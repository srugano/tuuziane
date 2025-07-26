# ruff: noqa: F405
from .base import *  # noqa: F403

DEBUG = False

# django-storages S3 configuration for production
# https://django-storages.readthedocs.io/en/latest/backends/amazon-S3.html
AWS_STORAGE_BUCKET_NAME = env("AWS_STORAGE_BUCKET_NAME")
AWS_S3_CUSTOM_DOMAIN = env("AWS_S3_CUSTOM_DOMAIN", default=f"{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com")
AWS_S3_OBJECT_PARAMETERS = {"CacheControl": "max-age=86400"}

STATIC_URL = f"https://{AWS_S3_CUSTOM_DOMAIN}/static/"
MEDIA_URL = f"https://{AWS_S3_CUSTOM_DOMAIN}/media/"

STORAGES.update(
    {
        "default": {
            "BACKEND": "storages.backends.s3boto3.S3Boto3Storage",
            "OPTIONS": {
                "location": "media",
                "file_overwrite": False,
            },
        },
        "staticfiles": {
            "BACKEND": "storages.backends.s3boto3.S3ManifestStaticStorage",
            "OPTIONS": {
                "location": "static",
            },
        },
    }
)

try:
    from .local import *  # noqa: F403
except ImportError:
    pass
