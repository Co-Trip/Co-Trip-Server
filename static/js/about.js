$(document).ready(function($) {
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