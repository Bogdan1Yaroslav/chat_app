from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from django.apps import apps

User = get_user_model()


class AppBlock(models.Model):
    DJANGO_APPS = [(app.name, app.verbose_name) for app in apps.get_app_configs() if not app.name.startswith("django")]

    app_name = models.CharField(max_length=300, choices=tuple(DJANGO_APPS))
    app_disable_reason = models.TextField()
    estimated_recovery_time = models.DateTimeField()

    class Meta:
        verbose_name_plural = "Блокировка приложений"
        verbose_name = "Блокировки приложений"


class Chat(models.Model):
    name = models.CharField(max_length=30)
    users = models.ManyToManyField(User, related_name='chats', through='UserChat')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('chat:room', args=[self.name])


class UserChat(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_chats')
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, related_name='user_chats')
    created_at = models.DateTimeField(auto_now_add=True)
    is_admin = models.BooleanField(default=False)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'chat'], name='Unique user in chat')
        ]

    def __str__(self):
        return f'Chat: {self.chat}'


class Message(models.Model):
    message = models.TextField()
    # Потом поменять on_delete чтобы сообщение сохранялось при удалении пользователя!
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='messages')
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, related_name='messages')
    sent_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.author.username}: {self.message} [{self.sent_at}]'
