import json
from channels.generic.websocket import AsyncWebsocketConsumer

class DonationConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        print('Consumers 1')
        await self.accept()
        await self.channel_layer.group_add("donation_updates", self.channel_name)

    async def donation_update(self, event):
        print('Consumers 2')
        message = event['message']

        await self.send(text_data=json.dumps({
            'message': message
        }))
