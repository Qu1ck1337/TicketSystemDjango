from rest_framework import status
from rest_framework.exceptions import NotFound
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response

from events.models import Event
from tickets.models import Ticket
from tickets.serializers import TicketSerializer


# Create your views here.
class TicketPurchaseAPIView(CreateAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer

    def perform_create(self, serializer):
        event_id = self.kwargs.get('pk')

        try:
            event = Event.objects.get(event_id=event_id)

            if event.available_tickets <= 0:
                raise NotFound("No tickets available")

            serializer.save(event=event)
        except Event.DoesNotExist:
            raise NotFound("Event not found")

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        self.perform_create(serializer)

        return Response({"message": "Ticket successfully created."}, status=status.HTTP_201_CREATED)