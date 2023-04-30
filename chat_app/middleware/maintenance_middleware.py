from django.urls import resolve
from django.shortcuts import render

from chat.models import AppBlock


class MaintenanceMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        app = resolve(request.path)

        try:
            requested_app = AppBlock.objects.get(app_name=app.app_name)
            return render(request, 'chat/app_maintenance.html', {"requested_app": requested_app})

        except AppBlock.DoesNotExist:
            return self.get_response(request)
