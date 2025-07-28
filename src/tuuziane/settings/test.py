# ruff: noqa: F403
from .dev import *

# Use in-memory SQLite database for tests
DATABASES = {
    "default": {
        "ENGINE": "django.contrib.gis.db.backends.spatialite",
        "NAME": ":memory:",
    }
}

# Oscar API
# ruff : noqa : F405
MIDDLEWARE.remove("oscarapi.middleware.ApiGatewayMiddleWare")
