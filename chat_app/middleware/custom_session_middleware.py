from chat_app.utils import get_user, get_browser, get_device, get_user_ip, get_last_visited


class CustomSessionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            request.session['user'] = get_user(request)
            request.session['browser'] = get_browser(request)
            request.session['device'] = get_device(request)
            request.session['ip'] = get_user_ip(request)
            request.session['last_visited'] = get_last_visited()

        response = self.get_response(request)

        return response
