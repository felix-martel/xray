//var serverURL = 'http://localhost:7080/xray/';
console.log("Loading...");
var waveforms = {};
var waveformReady = false;

$(document).ready(function(){
  var containers = document.querySelectorAll('.waveform-container');
  console.log(containers.length);

  for (var i=0; i<containers.length; i++){
      var audio_container = containers[i];
      ws = loadAudio(audio_container);
      waveforms[audio_container.id] = ws;
  }
  waveformReady = true;

});

function loadAudio(audio_container, alt_color=false){
  console.log(audio_container.id)
  var audioURL = '../../../static/radio/audio/' + audio_container.innerHTML;
  var wave_color = 'rgba(255, 255, 255, 0.7)';
  var progress_color = 'white';
  if (alt_color){
    wave_color = 'lightgray';
    progress_color = '#00fa9f';
  }
  var ws = WaveSurfer.create({
    container: '#' + audio_container.id,
    waveColor: wave_color,
    progressColor: progress_color,
    cursorColor: 'transparent',
    barWidth: 3,
  });
  ws.load(audioURL);
  ws.on('ready', function () {
    console.log(audioURL + ' ready !');
  });
  return ws;
}

function togglePlayPause(el, target) {
  if (waveforms[target]){
    var ws = waveforms[target];
    ws.playPause();
  }
  else {
    console.log(target)
    var audio_container = document.getElementById(target);
    var alt_color = $(audio_container).hasClass("waveform-container-no-autoload");
    console.log(audio_container.className);
    ws = loadAudio(audio_container, alt_color);
    waveforms[target] = ws;
    ws.on('ready', function () {
      ws.play();
    });
  }
  $(el).find('.fa').toggleClass("fa-play fa-pause");
}

var gif = $('#looping-div');
var gif_url = gif.css('background-image');

function toggleLive(){
  var audio = document.getElementById('xray-stream');
  var icon = $('#now-playing-icon');
  console.log(gif_url);

  if (audio.paused || audio.duration == 0){
    audio.play();
    gif.css('background-image', gif_url);
  }
  else {
    audio.pause();
    gif.css('background-image', 'none');
  }

  icon.toggleClass("fa-pause fa-play");
}

function playPauseById(el, elementId){
  var audio = document.getElementById(elementId);
  var icon = $(el);
  if (audio.paused || audio.duration == 0){
    audio.play();
  }
  else {
    audio.pause();
  }
  icon.toggleClass("fa-play fa-pause");
}
