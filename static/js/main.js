var socket = io();
var anim = new Animation();

// DIRTY DIRTY GLOBALS TO FIX LATER
var mouseClickedFlag = false;
var mousePos = { x: 0, y: 0 };
var firstLoginFlag = false;

anim.setStage();
anim.startAnim();

socket.on('login', function(data){
  if( !data.authenticated && firstLoginFlag ){
    alert("Login Failed, please try again.");
    firstLoginFlag = true;
  }

  if( data.authenticated ){
    console.log(data.user.username);
  }
})

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

socket.emit("join", "asdf")
