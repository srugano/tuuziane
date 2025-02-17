from .base import *

try:
    from .local import *  # noqa
except ImportError:
    pass


# SECURITY WARNING: don't run with debug turned on in production!

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
