var pageEnum = ['loginscreen', 'pickscreen', 'gamescreen']

function loadPageById(id){
  for(var i = 0, iLen = pageEnum.length; i < iLen; i++){
    document.getElementById(pageEnum[i]).style.display = "none";
  }

  document.getElementById(id).style.display = "inline";
}

var waifus = [];

function pickWaifu(waifu, id){
  if( waifus.length >= 4 ){
    return
  }

  waifus.push(waifu);

  document.getElementById(id).style.borderColor = 'blue';

  if( waifus.length >= 4 ){
    socket.emit('pick', { char_ids: waifus });
  }
}

function getSpriteAsset(charid){
  switch(charid){
    case "Bleaku":
      return "/static/images/bleaku.png"
    case "Dontno":
      return "/static/images/dontno.png"
    case "Exconata":
      return "/static/images/ExConata.png"
    case "Loise":
      return "/static/images/Loise.png"
    case "Mayo":
      return "/static/images/Mayo.png"
    case "Moyuri":
      return "/static/images/Moyuri.png"
    case "RAM":
      return "/static/images/RAM.png"
    case "Ray":
      return "/static/images/Ray.png"
    case "Stabber":
      return "/static/images/Stabber.png"
    case "Winery":
      return "/static/images/Winery.png"
  }
}
