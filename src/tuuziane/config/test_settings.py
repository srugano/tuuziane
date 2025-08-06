from .settings import *  # noqa: F403

MIDDLEWARE.remove("oscarapi.middleware.ApiGatewayMiddleWare")  # noqa: F405
