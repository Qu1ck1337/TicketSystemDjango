from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView
from events.models import Event
from events.serializers import EventSerializer
from tickets.models import Ticket


# Create your views here.
class EventListAPIView(ListAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


# if we put pk in urls we can rid of get_object code
class EventDetailAPIView(RetrieveAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

    def get_object(self):
        event_id = self.kwargs.get('event_id')
        return Event.objects.get(event_id=event_id)