function loginWithName(){
  var name = prompt("Please enter your username", "Lewis Bobbermen")

  socket.emit('login', { username: name });
}

function joinGame(){
  socket.emit('join', "");

  socket.on('join', function(data){
    console.log(data);

  });

  loadPageById("gamescreen");
  anim.startAnim();
  anim.center();
}
