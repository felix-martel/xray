function toggleDisplay(elementId){
  $(elementId).toggle();
}

var deezerWidget = '<script>(function(d, s, id) {var js, djs = d.getElementsByTagName(s)[0];if (d.getElementById(id)) return;js = d.createElement(s); js.id = id;js.src = "http://e-cdn-files.deezer.com/js/widget/loader.js"; djs.parentNode.insertBefore(js, djs);}(document, "script", "deezer-widget-loader"));</script><div class="deezer-widget-player" data-src="http://www.deezer.com/plugins/player?format=classic&autoplay=true&playlist=true&width=900&height=350&color=F7404B&layout=dark&size=medium&type=playlist&id=<<deezer_id>>&app_id=1" data-scrolling="no" data-frameborder="0" data-allowTransparency="true" data-width="900" data-height="350"></div>';
var last_container = "";

function displayPlaylist(){
  console.log("Retrieving playlist...");
  var deezer_id = $(this).data('playlist');
  var container = $(this).data('selector');
  console.log("Playlist ID : " + deezer_id);
  console.log("Container ID : " + container);
  var widget = deezerWidget.replace('<<deezer_id>>', deezer_id);
  if (last_container != ""){
    $(last_container).html("");
  }
  last_container = container;
  console.log(last_container);
  $(container).html(widget);
  //$(container).addClass("playlist-container");
}

$('.playlist-player').on("click", displayPlaylist);
