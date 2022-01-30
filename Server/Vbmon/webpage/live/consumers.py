import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.groupname = 'dashboard'
        async_to_sync(self.channel_layer.group_add)(
            self.groupname,
            self.channel_name,
        )
        self.accept()

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.groupname,
            self.channel_name
        )

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        value1 = text_data_json['x']
        value2 = text_data_json['y']
        value3 = text_data_json['z']

        async_to_sync(self.channel_layer.group_send)(
            self.groupname,
            {
                'type': 'deprocessing',
                'value1': value1,
                'value2': value2,
                'value3': value3,
            }
        )

        print('>>>>', text_data)

        # pass

    def deprocessing(self, event):
        valOther1 = event['value1']
        valOther2 = event['value2']
        valOther3 = event['value3']
        async_to_sync(self.send(text_data=json.dumps(
            {'value1': valOther1, 'value2': valOther2, 'value3': valOther3})))
