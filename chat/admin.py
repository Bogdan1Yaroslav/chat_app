from django.contrib import admin
from django.contrib.sessions.models import Session

from .models import Chat, UserChat, Message


@admin.register(Session)
class SessionAdmin(admin.ModelAdmin):
    list_display = [
        "session_key",
        'expire_date',
        "get_session_user",
        "get_browser",
        "get_device",
        "get_last_ip",
        "get_last_visit"
    ]

    ordering = ['-expire_date']

    def get_session_user(self, obj):
        return obj.get_decoded().get('user')

    get_session_user.short_description = 'User'

    def get_browser(self, obj):
        return obj.get_decoded().get('browser')

    get_browser.short_description = 'Browser'

    def get_device(self, obj):
        return obj.get_decoded().get('device')

    get_device.short_description = 'Device'

    def get_last_ip(self, obj):
        return obj.get_decoded().get('ip')

    get_last_ip.short_description = 'IP'

    def get_last_visit(self, obj):
        return obj.get_decoded().get('last_visited')

    get_last_visit.short_description = 'Last visit'


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

    get_users.short_description = 'Users'


@admin.register(UserChat)
class UserChatAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "user",
        "chat",
        "created_at",
        "is_admin",
    ]


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    pass
