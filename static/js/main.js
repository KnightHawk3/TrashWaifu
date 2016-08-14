var socket = io();
var anim = new Animation();

// DIRTY DIRTY GLOBALS TO FIX LATER
var mouseClickedFlag = false;
var mousePos = { x: 0, y: 0 };
var firstLoginFlag = false;
var map = [];

var players = [];
var teams = [];

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
  map = data.grid;
  players = data.players;
  teams = data.teams;

  loadPageById('gamescreen');
  anim.setStage();
  anim.loadTeams();
  anim.startAnim();

  console.log(data);
});
