var pageEnum = ['loginscreen', 'pickscreen', 'gamescreen']

function loadPageById(id){
  for(var i = 0, iLen = pageEnum.length; i < iLen; i++){
    document.getElementById(pageEnum[i]).style.display = "none";
  }

  document.getElementById(id).style.display = "inline";
}

var waifus = [];

function pickWaifu(waifu, id){
  waifus.push(waifu);

  document.getElementById(id).style.borderColor = 'blue';

  if( waifus.length >= 4 ){
    console.log('pick')
    socket.emit('pick', { char_ids: waifus });
  }
}
