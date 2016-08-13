function loginWithName(name){
  socket.emit('login', { username: name });
}

function joinGame(){
  socket.emit('join', "");

  socket.on('join', function(data){
    console.log(data);


    anim.startAnim();
  })
}
