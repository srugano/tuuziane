from django.conf import settings


def vue_env(request):
    return {
        "VUE_VARS": settings.VUE_VARS,
    }
