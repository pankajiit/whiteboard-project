import json
from channels.generic.websocket import AsyncWebsocketConsumer

class WhiteboardConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.whiteboard_id = self.scope['url_route']['kwargs']['whiteboard_id']
        self.room_group_name = f'whiteboard_{self.whiteboard_id}'

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        data = json.loads(text_data)
        data['user'] = self.scope["user"].username
        await self.channel_layer.group_send(
            self.room_group_name,
            {"type": "draw_action", "data": data}
        )

    async def draw_action(self, event):
        data = event["data"]
        await self.send(text_data=json.dumps(data))
