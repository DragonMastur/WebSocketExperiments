var socket = io.connect('http://' + document.domain + ':' + location.port);
var USER = "default";

socket.on('connect', function() {
  socket.emit('connected', {user: USER});
});

window.onbeforeunload = function() {
  socket.emit('disconnecting', {user: USER});
};
