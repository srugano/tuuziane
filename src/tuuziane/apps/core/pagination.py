from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from django.utils.translation import gettext as _


class StandardPagination(PageNumberPagination):
    """Standard pagination class with custom response format"""

    page_size = 50
    page_size_query_param = "page_size"
    max_page_size = 500

    def get_paginated_response(self, data, message=None, filters=None):
        """Return paginated response with custom format"""
        return Response(
            {
                "status": "success",
                "message": message if message else _("Data retrieved successfully"),
                "data": {
                    "objects": data,
                    "pagination": {
                        "total_items": self.page.paginator.count,
                        "total_pages": self.page.paginator.num_pages,
                        "current_page": self.page.number,
                        "per_page": self.get_page_size(self.request),
                        "has_next": self.page.has_next(),
                        "has_previous": self.page.has_previous(),
                        "next_page_number": self.page.next_page_number() if self.page.has_next() else None,
                        "previous_page_number": self.page.previous_page_number() if self.page.has_previous() else None,
                    },
                    "filters": filters or {},
                },
            }
        )
