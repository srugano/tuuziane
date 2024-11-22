from django.apps import apps
from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from django.views.generic.base import TemplateView
from wagtail import urls as wagtail_urls
from wagtail.admin import urls as wagtailadmin_urls
from wagtail.documents import urls as wagtaildocs_urls

urlpatterns = [
    path("django-admin/", admin.site.urls),
    path("admin/", include(wagtailadmin_urls)),
    path("documents/", include(wagtaildocs_urls)),
    path("documents/", include(wagtaildocs_urls)),
    path(
        "about/",
        TemplateView.as_view(template_name="header-spaceship-variant-one.html"),
    ),
    path("", include(apps.get_app_config("oscar").urls[0])),
]


if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    # Serve static and media files from development server
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns = urlpatterns + [
    path("", include(wagtail_urls)),
]
