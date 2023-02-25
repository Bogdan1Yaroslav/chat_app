from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy

from chat.models import Chat
from .models import UserChat


def index(request):
    context = {}
    users_chats = UserChat.objects.filter(user=request.user.id).select_related('chat')
    context['users_chats'] = users_chats

    return render(request, 'chat/index.html', context)


def room(request, room_name):
    chat, created = Chat.objects.get_or_create(name=room_name)
    chat.users.add(request.user.id)
    context = {'chat': chat}

    return render(request, 'chat/room.html', context)


class LogInView(LoginView):
    template_name = "chat/login.html"

    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('chat:index')
