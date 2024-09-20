# How to run

### To start WSGI server
```commandline
python manage.py runserver
```

### To start ASGI server (WebSocket support)
```commandline
daphne -p 8001 ticket_system.asgi:application
```

# APIs
**GET:** `events/` - get the list of all events

**GET:** `events/<event_id>` - get the detailed information of the event by _**event_id**_
- `event_id` : UUID - uuid of event

**POST:** `events/<event_id>/buy/` - to purchase a ticket for the event
- `event_id` : UUID - uuid of event

Body parameters:
- `user` : INT - id of user

# WebSocket

`/ws/tickets/<event_id}>`
- `event_id` : UUID - uuid of event

# How to check WebSocket work

Run ASGI and WSGI server

Create an event in admin panel, then insert uuid to `event_id` in `frontend/websocket_test.js`

Then run `websocket_test.js`
```commandline
cd frontend/
node websocket_test.js
```

To check the work add a ticket through `events/<event_id>/buy/` post method or add in admin panel

Available tickets for the event will be displayed in every update for everyone who connected to WebSocket in specific event.
