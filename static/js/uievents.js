function loginWithName(name){
  socket.emit('login', { username: name });
}
