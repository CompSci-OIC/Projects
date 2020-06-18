# chat/consumers.py
import json
import os
from channels.generic.websocket import AsyncWebsocketConsumer
from .models import CustomGroup, CustomUser
from asgiref.sync import sync_to_async
os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name
        self.group = CustomGroup.objects.get(id = int(self.room_name))
        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        self.group.delete_user(self.user_id)
        self.group.save()
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'header': 'header',
                'message': self.user.name + "#" + str(self.user_id),
                'name': "disconnect"
            }
        )


    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        name = text_data_json['name']
        header = text_data_json['header']

        # Send message to room group
        if header == 'normal':
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': 'chat_message',
                    'header': header,
                    'message': message,
                    'name':name
                }
            )
        else:
            self.user_id = int(message)
            self.user = CustomUser.objects.get(id = int(self.user_id))
            self.group.add_user(self.user_id)
            self.group.save()
            print("lalala",self.user_id)
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': 'chat_message',
                    'header': 'header',
                    'message': self.user.name + "#"+str(self.user_id),
                    'name': "connect"
                }
            )

    # Receive message from room group
    async def chat_message(self, event):
        header = event['header']
        message = event['message']
        name = event['name']

            # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'header': header,
            'message': message,
            'name': name
        }))
