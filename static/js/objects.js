var GameObject = function(xpos, ypos, mvd, stats){
  this.pos = { x: xpos, y: ypos };
  this.goalpos = { x: xpos, y: ypos };
  this.movedistance = mvd;
  this.stats = stats;
}

GameObject.prototype.getMoveDistance = function(){
  return this.movedistance;
}

GameObject.prototype.setMoveTo = function( xpos, ypos ){
  var distanceToMove = Math.abs(this.pos.x - xpos) + Math.abs(this.pos.y - ypos);
  if( distanceToMove <= this.movedistance ){
    this.goalpos.x = xpos;
    this.goalpos.y = ypos;
    return 1;
  } else {
    return 0;
  }
}

GameObject.prototype.moveStep = function(){
  var xdif = this.goalpos.x - this.pos.x
  var ydif = this.goalpos.y - this.pos.y

  if( xdif != 0 ){
    this.pos.x += Math.sign(xdif);
  } else if( ydif != 0 ){
    this.pos.y += Math.sign(ydif);
  }

  return this.pos;
}
