from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django.db.models.signals import post_save
from django.dispatch import receiver

from events.consumers import TicketConsumer
from tickets.models import Ticket


@receiver(post_save, sender=Ticket)
def ticket_created(sender, instance, created, **kwargs):
    if created:
        channel_layer = get_channel_layer()

        event_id = instance.event.event_id
        new_ticket_count = instance.event.available_tickets

        async_to_sync(channel_layer.group_send)(
            f"event_{event_id}",
            {
                'type': 'ticket_count_update',
                'available_tickets': new_ticket_count
            }
        )