from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Chat(models.Model):
    name = models.CharField(max_length=30)
    users = models.ManyToManyField(User, related_name='chats', through='UserChat')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class UserChat(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_chats')
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, related_name='user_chats')
    created_at = models.DateTimeField(auto_now_add=True)
    is_admin = models.BooleanField(default=False)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'chat'], name='Unique user in chat')
        ]


class Message(models.Model):
    message = models.TextField()
    # Потом поменять on_delete чтобы сообщение сохранялось при удалении пользователя!
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='messages')
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, related_name='messages')
    sent_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.author.username}: {self.message} [{self.sent_at}]'
