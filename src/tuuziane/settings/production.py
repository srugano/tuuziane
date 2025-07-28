# ruff: noqa: F405
from .base import *  # noqa: F403

DEBUG = False

# --- OBSCURE PATHS ---
# Define your obscure paths here to easily reuse them.
# You can generate these with a random string generator.
STATIC_PATH_NAME = "ivyodufise-a7b3c"
MEDIA_PATH_NAME = "ivyiwanyu-f2d9x"


# --- Static Files Configuration (Served from this Server) ---
# The URL will now be /assets-a7b3c/ instead of /static/
STATIC_URL = f"/{STATIC_PATH_NAME}/"
# Ensure STATIC_ROOT is defined in base.py, e.g., STATIC_ROOT = BASE_DIR / "staticfiles"


# --- DigitalOcean Spaces Configuration (for Media Files) ---
AWS_ACCESS_KEY_ID = env("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = env("AWS_SECRET_ACCESS_KEY")
AWS_STORAGE_BUCKET_NAME = env("AWS_STORAGE_BUCKET_NAME")
AWS_S3_ENDPOINT_URL = env("AWS_S3_ENDPOINT_URL")
AWS_S3_CUSTOM_DOMAIN = env("AWS_S3_CUSTOM_DOMAIN")
AWS_S3_OBJECT_PARAMETERS = {"CacheControl": "max-age=86400"}
AWS_DEFAULT_ACL = "public-read"
AWS_S3_FILE_OVERWRITE = False

# --- Media URL (Points to DigitalOcean with obscure path) ---
MEDIA_URL = f"https://{AWS_S3_CUSTOM_DOMAIN}/"


# sorl-thumbnail settings
# Regenerates thumbnails if they already exist.
# This is useful for fixing permissions on existing thumbnails.
# It's recommended to remove this after the issue is resolved to avoid performance overhead.
THUMBNAIL_FORCE_OVERWRITE = True


# --- Django Storages Backends ---
STORAGES = {
    # Media files backend
    "default": {
        "BACKEND": "storages.backends.s3boto3.S3Boto3Storage",
        "OPTIONS": {
            "location": MEDIA_PATH_NAME,
            "file_overwrite": False,
        },
    },
    # Static files backend (local)
    "staticfiles": {
        "BACKEND": "django.contrib.staticfiles.storage.ManifestStaticFilesStorage",
    },
}

try:
    from .local import *  # noqa: F403
except ImportError:
    pass
