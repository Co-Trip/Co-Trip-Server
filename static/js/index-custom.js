$(document).ready(function($) {
	var num = Math.floor(Math.random() * 12 + 1);
	$('#background-image1').css('background-image', 'url(../Background/' + num + '.jpg)');
	$('#background-image1').fadeIn(2000);
	$('#background-mask').attr('src', '../Background/' + num + '.jpg');
	setInterval(function() {
		num = Math.floor(Math.random() * 12 + 1);
		jQuery.changeBackgroundImage(num);
	}, 8000);

	jQuery.showPanel($('#login'));
	$('#button-signup').click(function(event) {
		jQuery.showPanel($('#signup'));
		jQuery.hidePanel($('#login'));
	});
	$('#button-login').click(function(event) {
		jQuery.showPanel($('#login'));
		jQuery.hidePanel($('#signup'));
	});
});

jQuery.changeBackgroundImage = function(num) {
	if ($('#background-image1').is(":hidden")) {
		$('#background-image1').css('background-image', 'url(../Background/' + num + '.jpg)');
		$('#background-mask').attr('src', '../Background/' + num + '.jpg');
		$('#background-image2').fadeOut(2000);
		$('#background-image1').fadeIn(3000);
	} else {
		$('#background-image2').css('background-image', 'url(../Background/' + num + '.jpg)');
		$('#background-mask').attr('src', '../Background/' + num + '.jpg');
		$('#background-image1').fadeOut(2000);
		$('#background-image2').fadeIn(3000);
	};
};

jQuery.showPanel = function($panel) {
	$panel.delay(50).show('slow').animate({
		left: -20,
		opacity: 1
	}, '8000').animate({
		left: 0
	}, 'fast');
};
jQuery.hidePanel = function($panel) {
	$panel.animate({
		left: -20,
	}, 'fast').animate({
		left: 120,
		opacity: 0
	}, '6000').hide('fast');
};