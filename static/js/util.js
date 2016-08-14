function coordsfinder(x, y){
    var newx = x*65;
    var newy = y*65;
}

var pageEnum = ['loginscreen', 'pickscreen', 'gamescreen']

function loadPageById(id){
  for(var i = 0, iLen = pageEnum.length; i < iLen; i++){
    document.getElementById(pageEnum[i]).style.display = "none";
  }

  document.getElementById(id).style.display = "inline";
}

var waifus = [];

function pickWaifu(waifu){
  waifus.push(waifu);

  console.log(waifu);

  if( waifus.length >= 4 ){
    console.log("woo")
    socket.emit('pick', { charids: waifus });
  }
}
