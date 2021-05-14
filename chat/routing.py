from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    url(r'^ws/chat/addition1/', consumers.ChatConsumer),
    url(r'^ws/chat/(?P<room_name>\w+)/', consumers.ChatConsumer),
]