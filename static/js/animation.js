var Animation = function(){
  this.renderer = new PIXI.WebGLRenderer(1024, 768);
  this.renderer.backgroundColor = 0x3498db;

  document.body.appendChild(this.renderer.view);

  this.stage = new PIXI.Container();

  this.sprites = [];
  this.background = [];
}

Animation.prototype.startAnim = function(){
  var self = this;

  animate();

  for(var i = 0, iLen = this.sprites.length; i < iLen; i++ ){
    this.stage.addChild(this.sprites[i]);
  }

  for(var i = 0, iLen = this.background.length; i < iLen; i++ ){
    this.stage.addChild(this.background[i]);
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

Animation.prototype.setStage = function(){
  var xDim = 30;
  var yDim = 20;

  var tileWidth = 64;

  for(var x = 0; x < xDim; x++ ){
    for(var y = 0; y < yDim; y++){
      var texture = PIXI.Texture.fromImage('static/images/floor.png');
      var tile = new PIXI.Sprite(texture);

      tile.anchor.x = 0.5;
      tile.anchor.y = 0.5;

      tile.position.x = x * 65;
      tile.position.y = y * 65;

      this.background.push(tile);
    }
  }
}
