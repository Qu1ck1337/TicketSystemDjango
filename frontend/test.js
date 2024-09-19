const WebSocket = require('ws');
const eventId = "7c1f0071-0411-4756-84d5-597fabafdf38";  // ID ивента
const socket = new WebSocket(`ws://localhost:8001/ws/tickets/${eventId}/`);

socket.onopen = function(e) {
    console.log('WebSocket connection opened');
};

socket.onmessage = function(e) {
    const data = JSON.parse(e.data);
    const availableTickets = data.available_tickets;

    console.log("Available tickets: " + availableTickets);
};

socket.onclose = function(e) {
    console.log('WebSocket connection closed');
};

socket.onerror = function(err) {
    console.error('WebSocket error:', err);
};