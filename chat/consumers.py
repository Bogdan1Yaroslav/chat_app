import json
from asgiref.sync import sync_to_async
from channels.generic.websocket import AsyncJsonWebsocketConsumer
from .models import Chat, Message


class ChatConsumer(AsyncJsonWebsocketConsumer):

    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)
        self.room_name = None
        self.room_group_name = None
        self.room = None
        self.user = None

    async def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = "chat_%s" % self.room_name
        self.room = await self.get_chat(self.room_name)
        self.user = self.scope['user']

        # Join room group
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)

        await self.accept()

    @sync_to_async
    def get_chat(self, room_name):
        return Chat.objects.get(name=room_name)

    @sync_to_async
    def save_message(self, msg):
        Message.objects.create(message=msg, author=self.user, chat=self.room)
        print(f"Message has successfully saved! {msg}")
        # return Chat.objects.get(name=room_name)

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

        # Receive message from WebSocket

    async def receive_json(self, content, **kwargs):
        message = content['message']

        if not self.user.is_authenticated:
            return

        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name, {
                "type": "chat_message",
                "message": message,
                "user": self.user.username}
        )

        # Receive message from room group

    async def chat_message(self, event):
        message = event["message"]

        await self.save_message(message)

        # Send message to WebSocket
        # await self.send(text_data=json.dumps({"message": message}))
        await self.send(text_data=json.dumps(event))
