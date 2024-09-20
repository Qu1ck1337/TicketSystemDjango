import json
from channels.generic.websocket import AsyncWebsocketConsumer


# WebSocket consumer
class TicketConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.event_id = self.scope['url_route']['kwargs']['event_id']
        self.event_group_name = f'event_{self.event_id}'

        await self.channel_layer.group_add(
            self.event_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.event_group_name,
            self.channel_name
        )

    async def ticket_count_update(self, event):
        await self.send(text_data=json.dumps({
            'available_tickets': event['available_tickets']
        }))