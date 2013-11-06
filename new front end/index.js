$(document).ready(function(){
$("#login").click(function(){
$("#login_box").fadeToggle("slow");
});

$("#slideshow").css("overflow","hidden");
$("#slideshow-nav").css("visibility","visible");

$("#slideshow-nav a[href=#page1]").addClass("active");

$("#slideshow-nav").localScroll({target:"#slideshow",axis:"x"});
$("#slideshow-nav a").click(function(){
$("#slideshow-nav a").removeClass("active");
$(this).addClass("active");
});
});