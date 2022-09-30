from django.urls import path
from . import consumers

websocket_urlpatterns=[
    path('ws/wsc/<str:groupkaname>/',consumers.MyWebSocketConsumer.as_asgi()),
    path('ws/awsc/',consumers.MyAsyncWebSocketConsumer.as_asgi()),
]