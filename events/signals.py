from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from events.models import Event
from tickets.models import Ticket


@receiver(post_save, sender=Event)
def create_ticket_for_event(sender, instance, created, **kwargs):
    if created:
        Ticket.objects.create(event=instance, user=User.objects.first())