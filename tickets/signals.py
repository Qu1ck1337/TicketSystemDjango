from django.db.models.signals import post_save
from django.dispatch import receiver
from tickets.models import Ticket


@receiver(post_save, sender=Ticket)
def notify_user_ticket_purchase(sender, instance, created, **kwargs):
    if created:
        print('Ticket Purchase Confirmation\n',
              f'Thank you for purchasing a ticket for {instance.event.name}!')
        # send_mail(
        #     'Ticket Purchase Confirmation',
        #     f'Thank you for purchasing a ticket for {instance.event.name}!',
        #     'example@from.email',
        #     [instance.user.email],
        #     fail_silently=False,
        #     connection=None
        # )