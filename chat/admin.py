from django.contrib import admin

from .models import Chat, UserChat, Message


@admin.register(Chat)
class ChatAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "name",
        "get_users",
        "created_at"
    ]

    search_fields = ["name"]

    def get_users(self, obj):
        return "\n".join([user.username for user in obj.users.all()])


@admin.register(UserChat)
class UserChatAdmin(admin.ModelAdmin):
    pass


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    pass
