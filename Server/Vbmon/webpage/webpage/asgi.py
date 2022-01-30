"""
ASGI config for webpage project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
import live.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'webpage.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            live.routing.websocket_urlpatterns
        )
    )
    # Just HTTP for now. (We can add other protocols later.)
})
