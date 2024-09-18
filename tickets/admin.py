from django.contrib import admin
from tickets.models import Ticket, Event

# Register your models here.
@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('event_id', 'name', 'description', 'start_date', 'location', 'available_tickets')
    search_fields = ('event_id', 'name', 'description', 'start_date', 'location', 'available_tickets')
    list_filter = ('start_date', 'location', 'available_tickets')



@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ('ticket_id', "event", "user")
    search_fields = ('ticket_id', "event__name", "user__username")
    list_filter = ("event__name",)