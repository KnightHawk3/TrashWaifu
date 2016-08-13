function loginWithName(name){
  socket.emit('login', { username: name });
}

function joinGame(){
  socket.emit('list', "");
  console.log("send")
}

socket.on('list', function(data){
  console.log(data);
})
