function loginWithName(){
  var name = prompt("Please enter your username", "Lewis Bobbermen")

  socket.emit('login', { username: name });
}

function joinGame(){
  socket.emit('join', "");

  socket.on('join', function(data){
    console.log(data);
    map = data.game.grid;
    console.log(map);
  });

  loadPageById("gamescreen");
  anim.startAnim();
  anim.center();
}
