import logging
from rest_framework import status
from rest_framework.parsers import FormParser, JSONParser, MultiPartParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet
from apps.core.utils import get_serializer_errors, get_client_ip, parse_user_agent
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.mixins import (
    ListModelMixin,
    RetrieveModelMixin,
    CreateModelMixin,
    UpdateModelMixin,
    DestroyModelMixin,
)
from django.utils.translation import gettext_lazy as _
from apps.core.pagination import StandardPagination


class BaseViewMixin(APIView):
    logger = None
    logger_name = None
    event_type = None
    geoip = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.get_event_type()  # Init the event type
        self.log_info(f"Called '{self.__class__.__name__}'")

    def get_logger(self):
        if self.logger_name:
            self.logger = logging.getLogger(self.logger_name)

        if not self.logger:
            self.logger = logging.getLogger(__name__)

        return self.logger

    def get_audit_context(self, event_type=None, extra=None):
        request = getattr(self, "request", None)

        if not event_type:
            event_type = self.get_event_type()

        context = {
            "event_type": event_type,
            "status": "ATTEMPTED",
        }
        if request:
            ip_address = get_client_ip(self.request)
            user_agent = self.request.META.get("HTTP_USER_AGENT", "")[:500]

            # Get location and device info
            # geoip = self.get_geoip()
            # location = geoip.get_location(ip_address)
            device_info = parse_user_agent(self.request)
            context.update(
                {
                    "http_method": self.request.method,
                    "path": self.request.path,
                    "ip": ip_address,
                    "user_agent": user_agent,
                    "user_id": str(getattr(self.request.user, "id", "")),
                    # "location": location,
                    "device": device_info,
                }
            )
        if extra:
            context.update(extra)
        return context

    def get_event_type(self):
        if not self.event_type:
            try:
                action = getattr(self, "action", "")
                self.event_type = f"{self.__class__.__name__}.{self.request.method.lower()}.{action}"
                self.event_type = self.event_type.strip(".")  # in case no action
            except Exception:
                # Called without request
                return f"{self.__class__.__name__}"
        return self.event_type

    def log(self, message, logger_method, event_type=None, audit_context=None):
        logger = self.get_logger()
        logger_method = getattr(logger, logger_method, logger.info)
        if not audit_context:
            audit_context = {}
        event_type = audit_context.get("event_type", event_type)

        if not event_type:
            event_type = self.get_event_type()

        logger_method(message, extra=self.get_audit_context(event_type=event_type, extra=audit_context), exc_info=True)

    def log_info(self, message, event_type=None, audit_context=None):
        self.log(message, "info", event_type=event_type, audit_context=audit_context)

    def log_error(self, message, event_type=None, audit_context=None):
        self.log(message, "error", event_type=event_type, audit_context=audit_context)

    def log_critical(self, message, event_type=None, audit_context=None):
        self.log(message, "critical", event_type=event_type, audit_context=audit_context)

    def log_warning(self, message, event_type=None, audit_context=None):
        self.log(message, "warning", event_type=event_type, audit_context=audit_context)

    def log_debug(self, message, event_type=None, audit_context=None):
        self.log(message, "debug", event_type=event_type, audit_context=audit_context)

    def log_and_response(self, logger_method, message, audit_context, event_type, response_data, status_code):
        self.log(message, logger_method=logger_method, event_type=event_type, audit_context=audit_context)
        return Response(response_data, status=status_code)

    def handle_exception(
        self, error, audit_context=None, logger_method=None, event_type=None, message=None, status_code=None
    ):
        """
        Handle exceptions with appropriate status codes for known error types.
        Avoids returning 500 for known exceptions that should have specific status codes.
        """
        if not audit_context:
            audit_context = self.get_audit_context()

        # Check again if it is dict
        if not audit_context:
            audit_context = {}

        # Determine appropriate status code and failure reason based on exception type
        if status_code is None:
            status_code, failure_reason = self._get_exception_status_code(error)
        else:
            failure_reason = "SERVER_ERROR"

        audit_context.update(
            {
                "status": "FAILED",
                "failure_reason": failure_reason,
                "error": str(error or "An error occurred"),
                "exception_type": type(error).__name__,
            }
        )

        # Determine appropriate logger method based on exception type
        if logger_method is None:
            logger_method = "error" if status_code >= 500 else "warning"

        self.log(
            f"Request failed with message: {message or str(error)}",
            logger_method=logger_method,
            event_type=event_type,
            audit_context=audit_context,
        )

        # Get appropriate error message
        error_message = self._get_exception_message(error, message)

        response_data = {"status": "error", "message": error_message}

        # Only include error details for server errors (5xx) to avoid exposing sensitive info
        if status_code >= 500:
            response_data["error"] = str(error or _("An error occurred"))

        return Response(response_data, status=status_code)

    def _get_exception_status_code(self, error):
        """
        Determine appropriate status code and failure reason for different exception types.
        """
        from rest_framework.exceptions import (
            ValidationError,
            PermissionDenied,
            NotFound,
            AuthenticationFailed,
            NotAuthenticated,
            MethodNotAllowed,
            ParseError,
            UnsupportedMediaType,
        )
        from django.core.exceptions import ObjectDoesNotExist, ValidationError as DjangoValidationError
        from django.db import IntegrityError

        # Authentication/Authorization errors (4xx)
        if isinstance(error, AuthenticationFailed | NotAuthenticated):
            return status.HTTP_401_UNAUTHORIZED, "AUTHENTICATION_FAILED"
        if isinstance(error, PermissionDenied):
            return status.HTTP_403_FORBIDDEN, "PERMISSION_DENIED"

        # Validation errors (4xx)
        if isinstance(error, ValidationError | DjangoValidationError):
            return status.HTTP_400_BAD_REQUEST, "VALIDATION_ERROR"

        # Not found errors (4xx)
        if isinstance(error, NotFound | ObjectDoesNotExist):
            return status.HTTP_404_NOT_FOUND, "NOT_FOUND"

        # Method/Media type errors (4xx)
        if isinstance(error, MethodNotAllowed):
            return status.HTTP_405_METHOD_NOT_ALLOWED, "METHOD_NOT_ALLOWED"
        if isinstance(error, ParseError):
            return status.HTTP_400_BAD_REQUEST, "PARSE_ERROR"
        if isinstance(error, UnsupportedMediaType):
            return status.HTTP_415_UNSUPPORTED_MEDIA_TYPE, "UNSUPPORTED_MEDIA_TYPE"

        # Database integrity errors (4xx)
        if isinstance(error, IntegrityError):
            return status.HTTP_400_BAD_REQUEST, "INTEGRITY_ERROR"

        # Default to server error (5xx)
        return status.HTTP_500_INTERNAL_SERVER_ERROR, "SERVER_ERROR"

    def _get_exception_message(self, error, custom_message=None):
        """
        Get appropriate error message for different exception types.
        """
        from rest_framework.exceptions import (
            ValidationError,
            PermissionDenied,
            NotFound,
            AuthenticationFailed,
            NotAuthenticated,
            MethodNotAllowed,
            ParseError,
            UnsupportedMediaType,
        )
        from django.core.exceptions import ObjectDoesNotExist, ValidationError as DjangoValidationError
        from django.db import IntegrityError
        from django.http.response import Http404

        # Use custom message if provided
        if custom_message:
            return custom_message

        # Authentication/Authorization messages
        if isinstance(error, AuthenticationFailed | NotAuthenticated):
            return _("Authentication failed. Please check your credentials.")
        if isinstance(error, PermissionDenied):
            return _("You do not have permission to perform this action.")
        if isinstance(error, Http404):
            return str(error)

        # Validation messages
        if isinstance(error, ValidationError | DjangoValidationError):
            try:
                # Try to get detail from DRF ValidationError
                if hasattr(error, "detail"):
                    detail = getattr(error, "detail", None)
                    if detail:
                        return str(detail)
            except Exception:
                ...

            try:
                # Try to get messages from Django ValidationError
                if hasattr(error, "messages"):
                    messages = getattr(error, "messages", [])
                    if messages and len(messages) > 0:
                        return str(messages[0])
            except Exception:
                ...

            try:
                # Try to get message_dict from Django ValidationError
                if hasattr(error, "message_dict"):
                    message_dict = getattr(error, "message_dict", {})
                    if message_dict:
                        return _("Validation error occurred.")
            except Exception:
                ...

            return _("Validation error occurred.")

        # Not found messages
        if isinstance(error, NotFound | ObjectDoesNotExist):
            return _("Requested resource not found.")

        # Method/Media type messages
        if isinstance(error, MethodNotAllowed):
            return _("Method not allowed.")
        if isinstance(error, ParseError):
            return _("Invalid request format.")
        if isinstance(error, UnsupportedMediaType):
            return _("Unsupported media type.")

        # Database integrity messages
        if isinstance(error, IntegrityError):
            return _("Data integrity error occurred.")

        # Default message
        return _("An error occurred.")

    def serializer_error_response(self, serializer, audit_context, event_type=None, logger_method=None, message=None):
        audit_context.update(
            {"status": "FAILED", "failure_reason": "VALIDATION_ERROR", "validation_errors": serializer.errors}
        )
        if logger_method is None:
            logger_method = "warning"
        self.log(
            message or "Validation failed",
            logger_method=logger_method,
            event_type=event_type,
            audit_context=audit_context,
        )
        error_string = get_serializer_errors(serializer.errors)
        return Response({"status": "error", "message": error_string}, status=status.HTTP_400_BAD_REQUEST)

    def create_monitoring_record(self, user, action, status, description, metadata=None, risk_level="LOW"):
        # """Create a monitoring record for audit purposes"""
        # try:
        #     ip_address = get_client_ip(self.request)
        #     user_agent = self.request.META.get('HTTP_USER_AGENT', '')[:500]

        #     monitoring_data = {
        #         "user": user,
        #         "action": action,
        #         "status": status,
        #         "description": description,
        #         "ip_address": ip_address,
        #         "user_agent": user_agent,
        #         "risk_level": risk_level
        #     }

        #     if metadata:
        #         monitoring_data["metadata"] = metadata

        #     Monitoring.objects.create(**monitoring_data)  # type: ignore
        # except Exception as e:
        #     self.log_error(f"Failed to create monitoring record: {str(e)}")
        ...

    def create_tracker_record(self, email, status="ATTEMPTED", metadata=None):
        """Create a tracker record for request tracking"""
        # try:
        #     ip_address = get_client_ip(self.request)
        #     user_agent = self.request.META.get("HTTP_USER_AGENT", "")[:500]
        #     # geoip = self.get_geoip()
        #     # location = geoip.get_location(ip_address)
        #     device_info = parse_user_agent(self.request)

        #     tracker_data = {
        #         "email": email,
        #         "ip": ip_address,
        #         "device": device_info,
        #         # "location": location,
        #         "status": status,
        #         "metadata": {
        #             "user_agent": user_agent,
        #             "path": self.request.path,
        #             "method": self.request.method,
        #             **(metadata or {}),
        #         },
        #     }

        #     Tracker.objects.create(**tracker_data)  # type: ignore
        # except Exception as e:
        #     self.log_error(f"Failed to create tracker record: {str(e)}")

    def success_response(self, message, data=None, status_code=status.HTTP_200_OK, audit_context=None):
        """Standard success response with logging"""
        response_data = {"status": "success", "message": message, "data": data}
        if audit_context:
            audit_context.update({"status": "SUCCESS"})
            self.log_info(f"Operation successful: {message}", audit_context=audit_context)
        return Response(response_data, status=status_code)

    def error_response(self, message, status_code=status.HTTP_400_BAD_REQUEST, audit_context=None, error_code=None):
        """Standard error response with logging"""
        response_data = {"status": "error", "message": message}
        if error_code:
            response_data["error_code"] = error_code

        if audit_context:
            audit_context.update({"status": "FAILED"})
            self.log_warning(f"Operation failed: {message}", audit_context=audit_context)

        return Response(response_data, status=status_code)

    def get_permissions(self):
        """
        Return the list of permissions that this view requires.
        Looks for <action>_permission_classes attribute.
        """
        action = getattr(self, "action", None)
        if action:
            attr = f"{action}_permission_classes"
            if hasattr(self, attr):
                return [perm() for perm in getattr(self, attr)]
        # Fallback to default
        if hasattr(super(), "get_permissions"):
            return super().get_permissions()
        return []

    def get_serializer_class(self):
        """
        Return the serializer class to use for the request.
        Looks for <action>_serializer_class attribute.
        """
        action = getattr(self, "action", None)
        if action:
            attr = f"{action}_serializer_class"
            if hasattr(self, attr):
                return getattr(self, attr)
        # Fallback to default
        if hasattr(super(), "get_serializer_class"):
            return super().get_serializer_class()
        return None


class BaseViewSetMixin(
    BaseViewMixin,
    GenericViewSet,
    ListModelMixin,
    RetrieveModelMixin,
    CreateModelMixin,
    UpdateModelMixin,
    DestroyModelMixin,
):
    """Enhanced ViewSet mixin with all BaseViewMixin capabilities"""

    pagination_class = StandardPagination
    parser_classes = [MultiPartParser, FormParser, JSONParser]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = None  # To be set in subclasses
    search_fields: list[str] = []  # To be set in subclasses
    ordering_fields: list[str] = []  # To be set in subclasses
    ordering = ["-date_created"]

    def get_paginated_response(self, queryset, serializer_class=None, message=None, filters=None, audit_context=None):
        monitoring_action = "LIST_OPERATION"
        try:
            paginator = self.pagination_class()
            if serializer_class is None:
                serializer_class = self.get_serializer_class()
                if serializer_class is None:
                    raise ValueError("No serializer class available")

            page = paginator.paginate_queryset(queryset, self.request)
            if page is not None:
                serializer = serializer_class(page, many=True)
                if audit_context is None:
                    audit_context = self.get_audit_context(monitoring_action)
                audit_context.update(
                    {
                        "status": "SUCCESS",
                        "total_items": paginator.page.paginator.count,
                        "total_pages": paginator.page.paginator.num_pages,
                        "current_page": paginator.page.number,
                        "page_size": len(page),
                    }
                )
                if paginator.page.paginator.count > 0:
                    self.create_monitoring_record(
                        user=self.request.user,
                        action=monitoring_action,
                        status="SUCCESSFUL",
                        description=f"Listed {len(page)} items from {self.__class__.__name__}",
                        metadata=audit_context,
                    )
                # Add applied filters/search/sort to response
                applied_filters = self._get_applied_filters()
                return paginator.get_paginated_response(serializer.data, message=message, filters=applied_filters)

            # If no pagination, serialize all queryset
            if serializer_class is None:
                raise ValueError("No serializer class available")
            serializer = serializer_class(queryset, many=True)
            if audit_context is None:
                audit_context = self.get_audit_context(monitoring_action)
            audit_context.update({"status": "SUCCESS", "total_items": queryset.count()})
            self.create_monitoring_record(
                user=self.request.user,
                action=monitoring_action,
                status="SUCCESSFUL",
                description=f"Listed {queryset.count()} items from {self.__class__.__name__}",
                metadata=audit_context,
            )
            applied_filters = self._get_applied_filters()
            return self.success_response(
                message=message,
                data={
                    "objects": serializer.data,
                    "pagination": {
                        "total_items": queryset.count(),
                        "total_pages": 1,
                        "current_page": 1,
                        "per_page": queryset.count(),
                        "has_next": False,
                        "has_previous": False,
                        "next_page_number": None,
                        "previous_page_number": None,
                    },
                    "filters": applied_filters,
                },
                audit_context=audit_context,
            )
        except Exception as e:
            if audit_context is None:
                audit_context = self.get_audit_context(monitoring_action)
            return self.handle_exception(e, audit_context, message="Failed to retrieve data")

    def _get_applied_filters(self):
        params = self.request.query_params
        filters = {}
        # If using a filterset, get its fields
        if hasattr(self, "filterset_class") and self.filterset_class:
            try:
                filter_fields = self.filterset_class.get_filters()
                if filter_fields:
                    for field_name in filter_fields:
                        if field_name in params:
                            filters[field_name] = params.get(field_name)
            except Exception:
                # If get_filters() fails, continue without filterset fields
                ...
        # Add search and ordering
        search = params.get("search")
        ordering = params.get("ordering")
        return {
            "filters": filters,
            "search": search,
            "ordering": ordering,
        }

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        model_name = getattr(instance._meta, "verbose_name", instance.__class__.__name__)
        instance_str = str(instance)
        message = f"found element {model_name} {instance_str}"
        return self.success_response(message=message, data=serializer.data)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop("partial", False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        model_name = getattr(instance._meta, "verbose_name", instance.__class__.__name__)
        instance_str = str(serializer.instance)
        message = f"updated element {model_name} {instance_str}"
        return self.success_response(message=message, data=serializer.data)

    def partial_update(self, request, *args, **kwargs):
        kwargs["partial"] = True
        return self.update(request, *args, **kwargs)
