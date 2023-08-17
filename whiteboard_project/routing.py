from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
from whiteboard_app.consumers import WhiteboardConsumer


application = ProtocolTypeRouter({
    'websocket': URLRouter([
        path('ws/whiteboard/<str:whiteboard_id>/', WhiteboardConsumer.as_asgi()),
    ]),
})
