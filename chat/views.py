from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.shortcuts import get_object_or_404
from django.http import HttpResponseNotFound
from django.urls import reverse_lazy

from chat.models import Chat
from django.http import Http404


def index(request):
    return render(request, 'chat/index.html')


def room(request, room_name):
    # chat, created = Chat.objects.get_or_create(name=room_name)
    # print(chat, created)

    return render(request, 'chat/room.html', {
        'room_name': room_name
    })


class LogInView(LoginView):
    template_name = "chat/login.html"

    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('index')
