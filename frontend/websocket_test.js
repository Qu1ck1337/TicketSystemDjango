// Shows the changes of available tickets for Event


const WebSocket = require('ws');
const eventId = "";  // Event ID
const socket = new WebSocket(`ws://localhost:8001/ws/tickets/${eventId}/`);

socket.onopen = function(e) {
    console.log('WebSocket connection opened');
};

// Called when the websocket sending a message from server
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