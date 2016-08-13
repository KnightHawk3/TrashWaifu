var socket = io();
var anim = new Animation();
anim.addCharacter(200, 150, 'static/images/0.png');
anim.addCharacter(300, 150, 'static/images/5.png');
anim.startAnim();

socket.on('login', function(data){
  console.log(data);
})

socket.on('connect', function(data){
  console.log(data);
})
