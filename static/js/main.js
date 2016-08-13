var socket = io();
var anim = new Animation();
anim.setStage();
anim.addCharacter(200, 150, 'static/images/0.png');
anim.addCharacter(300, 150, 'static/images/5.png');
anim.startAnim();

socket.on('login', function(data){
  // if data is false, kys

  // if data is true, woooooooo
  console.log(data);
})

function loginMeme(name){
  socket.emit('login', { username: name })
}
