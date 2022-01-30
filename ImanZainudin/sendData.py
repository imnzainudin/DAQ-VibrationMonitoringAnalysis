import websocket
import random
import time
import json
import requests
import getData

ws = websocket.WebSocket()

ws.connect('ws://localhost:8000/live/ws/chat/')

while(True):
    print (getData.main())
    ws.send(json.dumps(
        {'x': random.randint(1,100),
        'y': random.randint(1,100),
        'z': random.randint(1,100),
        }))
