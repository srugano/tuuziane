from django.apps import apps
from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from django.contrib.auth.views import LogoutView
from wagtail import urls as wagtail_urls
from wagtail.admin import urls as wagtailadmin_urls
from wagtail.documents import urls as wagtaildocs_urls

urlpatterns = [
    path("i18n/", include("django.conf.urls.i18n")),
    path("django-admin/", admin.site.urls),  # Django admin
    path("admin/", include(wagtailadmin_urls)),  # Wagtail admin
    path("documents/", include(wagtaildocs_urls)),  # Wagtail document downloads
    path(r"health/", include("health_check.urls")),  # Health check (good practice!)
    path("", include(apps.get_app_config("oscar").urls[0])),
    path("api/v1/", include("apps.catalogue.urls")),
    path("api/v1/osc/", include("oscarapi.urls")),
    # Wagtail's catch-all *last*
    path("", include(wagtail_urls)),
    path("logout/", LogoutView.as_view(next_page="/catalogue/"), name="logout"),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
