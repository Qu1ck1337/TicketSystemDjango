"""
ASGI config for ticket_system project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
"""

import os

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
from ticket_system import routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ticket_system.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    # Adding WebSocket support
    "websocket": AuthMiddlewareStack(
        URLRouter(
            routing.websocket_urlpatterns
        )
    ),
})
