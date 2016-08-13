var socket = io();
var anim = new Animation();


// DIRTY DIRTY GLOBALS TO FIX LATER
var mouseClickedFlag = false;
var mousePos = { x: 0, y: 0 };

anim.setStage();
anim.addCharacter(200, 150, 'static/images/0.png');
anim.addCharacter(300, 150, 'static/images/5.png');
anim.startAnim();

window.addEventListener('mousedown', function(event) {
  mouseClickedFlag = true;
  mousePos = { x: event.pageX, y: event.pageY };
})

socket.on('login', function(data){
  // if data is false, kys

  // if data is true, woooooooo
  console.log(data);
})

window.addEventListener('mouseup', function() {
  mouseClickedFlag = false;
})

window.addEventListener('mousemove', function(event) {
  if( mouseClickedFlag ){
    anim.moveStage( event.pageX - mousePos.x, event.pageY - mousePos.y );
    mousePos = { x: event.pageX, y: event.pageY };
  }
})
