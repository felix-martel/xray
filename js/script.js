var playEl = $("#play-button");
var el = $('#xray');
var audio = document.getElementById('xray-stream');
playEl.on("mouseeenter", function(){
  el.toggleClass("fa-play fa-pause");
});
playEl.on("mouseleave", function(){
  el.toggleClass("fa-play fa-pause");
});

playEl.on("click", function(){
if (audio.paused || audio.duration == 0){
	audio.play();
  el.toggleClass("fa-pause");
  el.toggleClass("fa-play");
	el.addClass("playing");
}
else {
	audio.pause();
  el.toggleClass("fa-pause");
  el.toggleClass("fa-play");
	el.addClass("playing");
}});

// -- Sleep mode -- //

var vol = 1.0;
var interval = 100;
var duration = 15 * 60 * 1000;
var step = (vol * interval) / duration; //var step = 0.05;
//
//var prog = document.getElementById('progress');

function setDuration(d){
  duration = d * 60 * 1000;
}

function fadeout(){
	prog.classList.remove("hidden");
	document.getElementById('sleep').classList.remove("fa-clock-o");
	document.getElementById('sleep').classList.add("fa-times");
	var sleep = setInterval(function() {
	if (vol > step){
		vol -=  step;
		audio.volume = vol;
		prog.value = 1 - vol;
    //$('#progress').css("width", 1 - vol);
    console.log(vol);
	}
	else {
		audio.volume = 0;
		prog.value = 1;
		audio.pause();
		audio.volume = 1;
		prog.classList.add("hidden");
		document.getElementById('sleep').classList.remove("fa-times");
		document.getElementById('sleep').classList.add("fa-clock-o");
		el.classList.remove("playing");
		clearInterval(sleep);
	}}, interval);
}


var triggerSleep = document.getElementById('sleep');
triggerSleep.addEventListener("click", fadeout);
