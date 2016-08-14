var socket = io();
var anim = new Animation();

// DIRTY DIRTY GLOBALS TO FIX LATER
var mouseClickedFlag = false;
var mousePos = { x: 0, y: 0 };
var firstLoginFlag = false;
var map = [];

window.addEventListener('mousedown', function(event) {
  mouseClickedFlag = true;
  mousePos = { x: event.pageX, y: event.pageY };
})

window.addEventListener('mouseup', function() {
  mouseClickedFlag = false;
})

window.addEventListener('mousemove', function(event) {
  if( mouseClickedFlag ){
    anim.moveStage( event.pageX - mousePos.x, event.pageY - mousePos.y );
    mousePos = { x: event.pageX, y: event.pageY };
  }
  anim.mousePosition(event.pageX, event.pageY);
})

socket.on('start', function(data){
  var map = data.grid;
  var players = data.players;
  var teams = data.teams;

  console.log(data);
});
