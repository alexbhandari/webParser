$(document).ready(function(){
$(".images").mouseover(function(){
$(this).css("background-color","#2E9AFE");
});
$(".images").mouseleave(function(){
$(this).css("background-color","#0B2161");
});


$("#urlinput-button").mousedown(function(){
$(this).css("background","linear-gradient(to bottom,#0B2161,#2E9AFE)");
});
$("#urlinput-button").mouseup(function(){
$(this).css("background","linear-gradient(to bottom,#2E9AFE,#0B2161)");
});
});