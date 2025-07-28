from django_user_agents.utils import get_user_agent  # type: ignore


def parse_user_agent(request):
    user_agent = get_user_agent(request)

    return {
        "device_type": "mobile" if user_agent.is_mobile else "tablet" if user_agent.is_tablet else "desktop",
        "browser": user_agent.browser.family,
        "browser_version": user_agent.browser.version_string,
        "os": user_agent.os.family,
        "os_version": user_agent.os.version_string,
        "device": user_agent.device.family,
        "is_bot": user_agent.is_bot,
    }


def get_client_ip(request):
    """Gets the client IP from the request object set by IpWareMiddleware."""
    return getattr(request, "IPWARE_CLIENT_IP", None)


def get_serializer_errors(serializer_errors):
    """Convert serializer error dictionary into a single string"""
    error_messages = []
    for field, errors in serializer_errors.items():
        if isinstance(errors, list):
            error_messages.append(f"{field}: {', '.join(errors)}")
        else:
            error_messages.append(f"{field}: {str(errors)}")
    return "; ".join(error_messages)
