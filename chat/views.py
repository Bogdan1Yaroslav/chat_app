from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy

from chat.models import Chat, Message
from .models import UserChat


class LogInView(LoginView):
    template_name = "chat/login.html"

    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('chat:select_chat')


class LogOutView(LogoutView):
    next_page = "/login"


@login_required(login_url='/login')
def select_chat(request):
    context = {}
    users_chats = UserChat.objects.filter(user=request.user.id).select_related('chat')
    context['users_chats'] = users_chats

    return render(request, 'chat/index.html', context)


@login_required(login_url='/login')
def room(request, room_name):
    chat, created = Chat.objects.get_or_create(name=room_name)
    messages = Message.objects.filter(chat=chat)
    chat.users.add(request.user.id)
    context = {'chat': chat, 'messages': messages}

    return render(request, 'chat/room.html', context)
