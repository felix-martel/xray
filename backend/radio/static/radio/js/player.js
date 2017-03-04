//var serverURL = 'http://localhost:7080/xray/';
console.log("Loading...");
var waveforms = {};
var waveformReady = false;

$(document).ready(function(){
  var containers = document.querySelectorAll('.waveform-container');
  console.log(containers.length);

  for (var i=0; i<containers.length; i++){
      var audio_container = containers[i];
      console.log(audio_container.id)
      var audioURL = '../../../static/radio/audio/' + audio_container.innerHTML;
      var ws = WaveSurfer.create({
        container: '#' + audio_container.id,
        waveColor: 'rgba(200, 200, 200, 1.0)',
        progressColor: '#cc0000',
        cursorColor: 'transparent',
        barWidth: 3,
      });
      ws.load(audioURL);
      ws.on('ready', function () {
        console.log(audioURL + ' ready !');
      });
      waveforms[audio_container.id] = ws;
  }
  waveformReady = true;

});

function togglePlayPause(el, target) {
  if (waveformReady){
    var ws = waveforms[target];
    ws.playPause();

    $(el).find('.fa').toggleClass("fa-play fa-pause");
  }
}
