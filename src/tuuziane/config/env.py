from smart_env import SmartEnv
from enum import Enum

NOT_SET = "<- not set ->"


class Group(Enum):
    DJANGO = 1


DEFAULTS = {
    # Core settings
    "ALLOWED_HOSTS": (list, ["localhost", "127.0.0.1"]),
    "ADMIN_PANEL_URL": (str, "rabangaha"),
    "DATABASE_URL": (str, "sqlite:///db.sqlite3"),
    "DEBUG": (bool, False),
    "DOMAIN": (str, "http://localhost:8000"),
    "SECRET_KEY": (str, "your-default-secret-key"),
    "WAGTAILADMIN_BASE_URL": (str, "http://localhost"),
    # Email settings
    "DEFAULT_FROM_EMAIL": (str, "webmaster@localhost"),
    "EMAIL_HOST": (str, ""),
    "EMAIL_HOST_USER": (str, ""),
    "EMAIL_HOST_PASSWORD": (str, ""),
    "EMAIL_PORT": (str, ""),
    "EMAIL_USE_TLS": (bool, True),
    # Storage settings
    "STORAGE_TYPE": (str, "local"),  # local or s3
    "SENTRY_DSN": (str, "", "https://develop.sentry.dev/config/"),
    "SENTRY_ENVIRONMENT": (str, NOT_SET, "https://develop.sentry.dev/config/"),
    "SENTRY_RELEASE": (str, ""),
    "SENTRY_TRACES_SAMPLE_RATE": (float, 1.0),
    "SENTRY_URL": (str, "https://jengamarket.com/sentry/hope-cr/", "Sentry server url"),
    "AWS_ACCESS_KEY_ID": (str, ""),
    "AWS_S3_CUSTOM_DOMAIN": (str, ""),
    "AWS_S3_ENDPOINT_URL": (str, ""),
    "AWS_SECRET_ACCESS_KEY": (str, ""),
    "AWS_STORAGE_BUCKET_NAME": (str, ""),
    "STATIC_PATH_NAME": (str, "static"),
    "MEDIA_PATH_NAME": (str, "media"),
    # Social auth
    "SOCIALACCOUNT_PROVIDERS": (
        dict,
        {
            "google": {"APP": {"client_id": "", "secret": "", "key": ""}},
            "facebook": {"APP": {"client_id": "", "secret": "", "key": ""}},
        },
    ),
    # Performance
    "THUMBNAIL_FORCE_OVERWRITE": (bool, False),
}

env = SmartEnv(**DEFAULTS)
