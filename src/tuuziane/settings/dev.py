import sys

from .base import *  # noqa: F403

try:
    from .local import *  # noqa
except ImportError:
    pass


# SECURITY WARNING: don't run with debug turned on in production!

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"


# Use in-memory SpatiaLite database for tests to speed them up
# and avoid OperationalError
if "test" in sys.argv or "pytest" in sys.argv[0]:
    DATABASES = {
        "default": {
            "ENGINE": "django.contrib.gis.db.backends.spatialite",
            "NAME": ":memory:",
        }
    }
