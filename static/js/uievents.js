function loginWithName(){
  var name = prompt("Please enter your username", "Lewis Bobbermen")

  socket.emit('login', { username: name });
}

function joinGame(){
  socket.emit('join', "");

  socket.on('join', function(data){
    map = data.game.grid;
    console.log(map);
    loadPageById("gamescreen");
    anim.setStage();
    anim.startAnim();
    anim.center();
  });
}

function playSound(file) {
  var audio = new Audio('static/sound/'+file);
  audio.play();
}
