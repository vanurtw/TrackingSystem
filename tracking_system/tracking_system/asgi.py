"""
ASGI config for tracking_system project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter
from channels.auth import AuthMiddlewareStack
from presence.consumers import PresenceConsumer
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tracking_system.settings')

application = ProtocolTypeRouter(
    {
        'http':get_asgi_application(),
        'websocket':AuthMiddlewareStack(
            PresenceConsumer.as_asgi()
        ),
    }
)