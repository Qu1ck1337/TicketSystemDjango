from django.urls import re_path
from events import consumers

websocket_urlpatterns = [
    re_path(r'ws/tickets/(?P<event_id>[0-9a-f-]+)', consumers.TicketConsumer.as_asgi()),
]