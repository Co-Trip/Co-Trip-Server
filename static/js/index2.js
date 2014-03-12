$(document).ready(function($) {
	var num = Math.floor(Math.random() * 12 + 1);
	$('#background-image1').css('background-image', 'url(../Background/' + num + '.jpg)');
	$('#background-image1').fadeIn(2000);
	$('#background-mask').attr('src', '../Background/' + num + '.jpg');
	setInterval(function() {
		num = Math.floor(Math.random() * 12 + 1);
		jQuery.changeBackgroundImage(num);
	}, 8000);

	$('.button-link').click(function(event) {
		var $parent = $(this).parent();
		if (!$parent.hasClass('active')) {
			$('.active').toggleClass('active');
		} else {
			$('.close').click();
		}
		$parent.toggleClass('active');
	});
	$('.modal.fade').on('hide.bs.modal', function (e) {
		$('div.button.active').toggleClass('active');
	})

	var loginForm = $('#login-form');
	loginForm.submit(function(event) {
		alert('submit!!!');
		$(this).ajaxSubmit({
			data: {'username': 'asdfads', 'password': 'sadfdsa'},
			dataType: 'json',
			target: '#login-form>.modal-body',
			type: 'POST'
		});
		return true;
	});

	var menuButtonOne = $('.menu-button').first();
	var leftSideMenu = $(menuButtonOne.data('target'));
	menuButtonOne.click(function(event) {
		leftSideMenu.show('fast');
		leftSideMenu.animate({
			left: 0, 
		}, 'fast', 'swing');
	});

	var menuButtonClose = $('.menu-close');
	menuButtonClose.click(function(event) {
		leftSideMenu.animate({
			left: -260, 
		}, 'fast');
		leftSideMenu.hide('fast');
		$('.active').toggleClass('active');
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