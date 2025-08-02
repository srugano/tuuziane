from django.apps import apps
from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from wagtail import urls as wagtail_urls
from wagtail.admin import urls as wagtailadmin_urls
from wagtail.documents import urls as wagtaildocs_urls
from tuuziane.core.views import AboutView, ContactView

urlpatterns = [
    path("i18n/", include("django.conf.urls.i18n")),
    path(f"{settings.ADMIN_PANEL_URL}/kurabaibintu/", admin.site.urls),  # Django admin
    path(f"{settings.ADMIN_PANEL_URL}/kwandika/", include(wagtailadmin_urls)),  # Wagtail admin
    path("documents/", include(wagtaildocs_urls)),  # Wagtail document downloads
    path("accounts/", include("allauth.urls")),
    path(r"health/", include("health_check.urls")),  # Health check (good practice!)
    path("about/", AboutView.as_view(), name="about"),
    path("contact/", ContactView.as_view(), name="contact"),
    # path("api/v1/", include("apps.catalogue.urls")),
    path("api/v1/osc/", include("oscarapi.urls")),
    path("raba/", include(wagtail_urls)),
    path("", include(apps.get_app_config("oscar").urls[0])),  # type: ignore [attr-defined]
]

if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    urlpatterns += staticfiles_urlpatterns()  # type: ignore
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # type: ignore
