# chat/consumers.py
import json
from channels.generic.websocket import AsyncWebsocketConsumer
from .models import CustomGroup, CustomUser

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name
        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
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
            print('pooop')

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
