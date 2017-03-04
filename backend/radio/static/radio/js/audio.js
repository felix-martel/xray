
window.AudioContext = 	window.AudioContext
|| window.webkitAudioContext
|| window.mozAudioContext;
var renderers = {
	'r3':(function(){
		var circles=[];
		var initialized=false;
		var height=0;
		var width=0;
		var init=function(config){
			var count=config.count;
			width=config.width;
			height=config.height;
			var circleMaxWidth=(width*0.66)>>0;
			circlesEl=document.getElementById('circles');
			for(var i=0;i<count;i++){
				var node=document.createElement('div');
				node.style.width=node.style.height=(i/count*circleMaxWidth)+'px';
				node.classList.add('circle');
				circles.push(node);
				circlesEl.appendChild(node);
			}
			initialized=true;
		};
		var max=256;
		var renderFrame=function(frequencyData){
			for(var i=0;i<circles.length;i++){
				var circle=circles[i];
				circle.style.cssText='-webkit-transform:scale('+((frequencyData[i]/max))+')';
			}};
			return{init:init,isInitialized:function(){return initialized;
			}, renderFrame:renderFrame}})()
}};
