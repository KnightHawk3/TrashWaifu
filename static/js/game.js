var Game = function(socket){
  this.socket = socket;
  this.team = [];

  this.pickflag = false;
}

Game.prototype.pickWaifu = function(waifu){
  if ( this.pickflag ) return;

  this.team.push(waifu);

  if( this.team.length >= 4 ){
    this.socket.emit('pick', { charids: this.team });
    this.pickflag = true;
  }
}
