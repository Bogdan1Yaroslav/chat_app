from datetime import datetime


def get_user(request) -> str:
    return request.user.username


def get_browser(request) -> str:
    return f"{request.user_agent.browser.family}"


def get_device(request) -> str:
    return f"{request.user_agent.os.family}"


def get_user_ip(request) -> str:
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


# def get_browser_version(request) -> str:
#     return f"{request.user_agent.browser.version_string}"


# def get_os_info(request) -> str:
#     return f"{request.user_agent.os.family} ver. {request.user_agent.os.version_string}"


def get_last_visited() -> str:
    return datetime.now().strftime("%d.%m.%Y %H:%M")
