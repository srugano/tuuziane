from django_user_agents.utils import get_user_agent
from ipware import get_client_ip as ipware_get_client_ip


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
    client_ip, is_routable = ipware_get_client_ip(request)
    if client_ip is None:
        return None
    else:
        # We got the client's IP address
        if is_routable:
            # The client's IP address is publicly routable on the Internet
            return client_ip
        else:
            # The client's IP address is private
            return None


def get_serializer_errors(serializer_errors):
    """Convert serializer error dictionary into a single string"""
    error_messages = []
    for field, errors in serializer_errors.items():
        if isinstance(errors, list):
            error_messages.append(f"{field}: {', '.join(errors)}")
        else:
            error_messages.append(f"{field}: {str(errors)}")
    return "; ".join(error_messages)
