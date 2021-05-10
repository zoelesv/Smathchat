"""
ASGI config for finalproject project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/asgi/
"""

import os
#import channels.asgi
#from django.core.asgi import get_asgi_application
#from channels.routing import ProtocolTypeRouter

#os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'finalproject.settings')
#application = ProtocolTypeRouter({
    #"http": get_asgi_application(),
    # Just HTTP for now. (We can add other protocols later.)
#})


#channel_layer = channels.asgi.get_channel_layer()
#application = get_asgi_application()

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
import chat.routing

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "finalproject.settings")
django.setup()
#application = get_default_application()

application = ProtocolTypeRouter({
  "http": get_asgi_application(),
  "websocket": AuthMiddlewareStack(
        URLRouter(
            chat.routing.websocket_urlpatterns
        )
    ),
})