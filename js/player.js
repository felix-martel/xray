
var ws = WaveSurfer.create({
  container: '#waveform',
  waveColor: 'rgba(255, 255, 255, 0.7)',
  progressColor: 'white',
});
ws.load('/audio/demo.mp3');
ws.on('ready', function (){
  wavesurfer.play();
})
