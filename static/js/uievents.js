function loginWithName(){
  username = prompt("Please enter your username", "Lewis Bobbermen")

  socket.emit('login', { username: username });

  socket.on('login', function(data){
    if (data.authenticated){
      document.getElementById("joinbutton").addEventListener("click", function() {
          socket.emit('join', "");
      })

      socket.on('join', function(data){
        gameid = data.game_id
        playSound('waifu_faito.mp3');
        loadPageById('pickscreen');
      });
    }
  })
}

function playSound(file) {
  var audio = new Audio('static/sound/'+file);
  audio.play();
}

function mouseOverCharacterArt(elem){
  var searchPic = new Image();
  searchPic.onload = function () {
    document.getElementById("splash").src = elem;
  }
  searchPic.src = elem;
}
