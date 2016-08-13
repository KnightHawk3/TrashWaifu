var Waifu = function(name, totalHealth, element, attack, defence, range, mvd, xpos, ypos){
  this.pos = { x: xpos, y: ypos };
  this.goalpos = { x: xpos, y: ypos };
  this.movedistance = mvd;
  //this.sprite = null;

  this.name = name;
  this.maxHealth = totalHealth;
  this.currentHealth = totalHealth;
  this.element = element;
  this.attack = attack;
  this.defence = defence;
  this.range = range;
}

Waifu.prototype.getMoveDistance = function(){
  return this.movedistance;
}

Waifu.prototype.setMoveTo = function( xpos, ypos ){
  var distanceToMove = Math.abs(this.pos.x - xpos) + Math.abs(this.pos.y - ypos);
  if( distanceToMove <= this.movedistance ){
    this.goalpos.x = xpos;
    this.goalpos.y = ypos;
    return 1;
  } else {
    return 0;
  }
}

Waifu.prototype.moveStep = function(){
  var xdif = this.goalpos.x - this.pos.x;
  var ydif = this.goalpos.y - this.pos.y;

  if( xdif != 0 ){
    this.pos.x += Math.sign(xdif);
  } else if( ydif != 0 ){
    this.pos.y += Math.sign(ydif);
  }

  return this.pos;
}

Waifu.prototype.takeDamage = function(damage) {
  this.currentHealth -= damage;
  if(this.currentHealth <= 0) {
    killWaifu();
  }
}

Waifu.prototype.killWaifu = function() {
  //destroy object, play animation?
}


// Waifu.prototype.setSprite = function(path){
//   //load texture from file
//
// }
//
// Waifu.prototype.getSprite = function() {
//   return this.sprite;
// }

Waifu.prototype.getName = function(){
  return this.name;
}

Waifu.prototype.getElement = function() {
  return this.element;
}

Waifu.prototype.getAttack = function(){
  return this.attack;
}

Waifu.prototype.getDefence = function(){
  return this.defence;
}

Waifu.prototype.getCurrentHealth = function(){
  return this.getCurrentHealth;
}

Waifu.prototype.getMaxHealth = function(){
  return this.maxHealth;
}
