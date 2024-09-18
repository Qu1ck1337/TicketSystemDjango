import uuid

from django.db import models

# Create your models here.
class Event(models.Model):
    event_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateTimeField()
    location = models.CharField(max_length=255)
    available_tickets = models.IntegerField()

    def __str__(self):
        return self.name
