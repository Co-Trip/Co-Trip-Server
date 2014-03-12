$(document).ready(function($) {
	var num = Math.floor(Math.random() * 3 + 2);
	$('#background-image1').css('background-image', 'url(../Background/' + num + '.jpg)');
	$('#background-image1').fadeIn(2000);
	$('#background-mask').attr('src', '../Background/' + num + '.jpg');
	setInterval(function() {
		num = Math.floor(Math.random() * 12 + 1);
		jQuery.changeBackgroundImage(num);
	}, 8000);

	$('#login-button').click(function(event) {
		$('.signup-block').fadeOut('fast', function() {
			$('.login-block').fadeIn('fast');
		});
	});
	$('#signup-button').click(function(event) {
		$('.login-block').fadeOut('fast', function() {
			$('.signup-block').fadeIn('fast');
		});
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