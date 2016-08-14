var socket = io();
var anim = new Animation();

// DIRTY DIRTY GLOBALS TO FIX LATER
var mouseClickedFlag = false;
var mousePos = { x: 0, y: 0 };
var firstLoginFlag = false;
var map = [];

var players = [];
var teams = [];
var selectedWaifu = { i: -1, j: -1 };

window.addEventListener('mousedown', function(event) {
  mouseClickedFlag = true;
  mousePos = { x: event.pageX, y: event.pageY };
})

window.addEventListener('mouseup', function() {
  mouseClickedFlag = false;
})

window.addEventListener('mousemove', function(event) {
  if( mouseClickedFlag ){
    anim.moveStage( event.pageX - mousePos.x, event.pageY - mousePos.y );
    mousePos = { x: event.pageX, y: event.pageY };
  }
  anim.mousePosition(event.pageX, event.pageY);
})

socket.on('start', function(data){
  map = data.grid;
  players = data.players;
  teams = data.teams;

  loadPageById('gamescreen');
  anim.setStage();
  anim.loadTeams();
  anim.startAnim();

  setTimeout( function() {
  document.addEventListener('mousedown', function(data){
    var pos = anim.getMouseOverTile();

    if(selectedWaifu.i != -1){
      teams[selectedWaifu.i][selectedWaifu.j].position[0] = pos.x;
      teams[selectedWaifu.i][selectedWaifu.j].position[1] = pos.y;
      anim.setSpritePos(pos, (selectedWaifu.i * 4) + selectedWaifu.j );
      selectedWaifu = { i: -1, j: -1 };
      anim.setPathFindingOrigin(0, 0);
      return
    }
    var waifuTeam;
    var waifuNumber;

    for(var i = 0, iLen = teams.length; i < iLen; i++){
      for(var j = 0, jLen = teams[i].length; j < jLen; j++){
        if(teams[i][j].position[0] == pos.x && teams[i][j].position[1] == pos.y) {
          waifuTeam = i;
          waifuNumber = j;
        }
      }
    }

    // team check later
    if(waifuTeam != undefined){
      anim.setPathFindingOrigin(pos.x, pos.y);
    }

    selectedWaifu.i = waifuTeam;
    selectedWaifu.j = waifuNumber;
  }) }, 300);

  console.log(data);
});
