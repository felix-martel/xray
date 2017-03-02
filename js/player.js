//var serverURL = 'http://localhost:7080/xray/';
var audioURL = 'audio/demo.mp3';
var ws = WaveSurfer.create({
  container: '#waveform',
  waveColor: 'rgba(255, 255, 255, 0.7)',
  progressColor: 'white',
  cursorColor: 'transparent',
});
ws.load(audioURL);
ws.on('ready', function (){
  ws.setVolume(0.03);
  //ws.play();
});
