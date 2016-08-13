var Animation = function(){
  this.renderer = new PIXI.WebGLRenderer(window.innerWidth, window.innerHeight );
  this.renderer.backgroundColor = 0x778899;

  this.boardSize = { x: 15, y: 10 }

  document.body.appendChild(this.renderer.view);

  this.stage = new PIXI.Container();

  this.mouseOverTile = { x: 0, y: 0 }

  this.sprites = [];
  this.background = [];
}

Animation.prototype.startAnim = function(){
  var self = this;

  animate();

  for(var i = 0, iLen = this.background.length; i < iLen; i++ ){
    this.stage.addChild(this.background[i]);
  }

  // ADD environment stuff here

  for(var i = 0, iLen = this.sprites.length; i < iLen; i++ ){
    this.stage.addChild(this.sprites[i]);
  }

  function animate() {
    requestAnimationFrame(animate);

    for(var i = 0, iLen = self.background.length; i < iLen; i++ ){
      self.background[i].tint = 0xFFFFFF;
    }

    var xyz = self.mouseOverTile.y + self.mouseOverTile.x * self.boardSize.y;

    if(xyz < self.boardSize.y * self.boardSize.x && xyz >= 0 ){
      self.background[ xyz ].tint = 0x3498db;
    }

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
  var tileWidth = 64;

  for(var x = 0; x < this.boardSize.x; x++ ){
    for(var y = 0; y < this.boardSize.y; y++){
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

Animation.prototype.moveStage = function(x, y){
  this.stage.x += x;
  this.stage.y += y;
}

Animation.prototype.mousePosition = function(x, y){
  var xpos = x - this.stage.x;
  var ypos = y - this.stage.y;

  var xtile = Math.floor((xpos/65) + 0.5);
  var ytile = Math.floor((ypos/65) + 0.5);

  this.mouseOverTile = { x: xtile, y: ytile };
}
