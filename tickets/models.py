import uuid
from django.contrib.auth.models import User
from django.db import models
from events.models import Event


# Create your models here.
class Ticket(models.Model):
    ticket_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    event = models.ForeignKey(Event, to_field='event_id', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if self._state.adding:  # Called when the ticked is created
            self.event.available_tickets -= 1
            self.event.save()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Ticket of {self.event} for {self.user}"