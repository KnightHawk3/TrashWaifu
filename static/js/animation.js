var Animation = function(){
  this.renderer = new PIXI.WebGLRenderer(1024, 768);
  this.renderer.backgroundColor = 0x3498db;

  document.body.appendChild(this.renderer.view);

  this.stage = new PIXI.Container();

  this.sprites = [];

}

Animation.prototype.startAnim = function(){
  var self = this;

  animate();

  for(var i = 0, iLen = this.sprites.length; i < iLen; i++ ){
    this.stage.addChild(this.sprites[i]);
  }

  function animate() {
    requestAnimationFrame(animate);

    self.sprites[0].rotation += 0.01;

    self.renderer.render(self.stage);
  }
}

Animation.prototype.addCharacter = function(x, y, textureURL){
  var texture = PIXI.Texture.fromImage(textureURL);
  var character = new PIXI.Sprite(texture);

  character.anchor.x = 0.5;
  character.anchor.y = 0.5;

  character.position.x = x;
  character.position.y = y;

  this.sprites.push(character);
}
