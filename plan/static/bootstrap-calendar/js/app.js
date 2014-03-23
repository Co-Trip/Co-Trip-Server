(function($) {

	"use strict";

	var options = {
		events_source: 'events/',
		view: 'month',
		tmpl_path: '/static/bootstrap-calendar/tmpls/',
		tmpl_cache: false,
		day: '2013-03-12',
		modal: '#events-modal',
		modal_type: 'template',
		language: 'zh-CN',
		onAfterEventsLoad: function(events) {
			if(!events) {
				return;
			}
			
			var list = $('#eventlist');
			list.html('');

			$.each(events, function(key, val) {
				$(document.createElement('li'))
					.html('<a href="' + val.url + '">' + val.title + '</a>')
					.appendTo(list);
			});
		},
		onAfterViewLoad: function(view) {
			$('.page-header h3').text(this.getTitle());
			$('.btn-group button').removeClass('active');
			$('button[data-calendar-view="' + view + '"]').addClass('active');
		},
		classes: {
			months: {
				general: 'label'
			}
		}
	};

	var calendar = $('#calendar').calendar(options);

	$('.btn-group button[data-calendar-nav]').each(function() {
		var $this = $(this);
		$this.click(function() {
			calendar.navigate($this.data('calendar-nav'));
		});
	});

	$('.btn-group button[data-calendar-view]').each(function() {
		var $this = $(this);
		$this.click(function() {
			calendar.view($this.data('calendar-view'));
		});
	});

	$('button[data-calendar-act]').each(function(index, el) {
		var $this = $(this);
		$this.click(function(event) {
			var modal = $('#add-events-modal');
			modal.modal('show');
		});
	});

	$('#first_day').change(function(){
		var value = $(this).val();
		value = value.length ? parseInt(value) : null;
		calendar.setOptions({first_day: value});
		calendar.view();
	});

	$('#language').change(function(){
		calendar.setLanguage($(this).val());
		calendar.view();
	});
	$('#events-modal .modal-header, #events-modal .modal-footer').click(function(e){
		//e.preventDefault();
		//e.stopPropagation();
	});

	var form = $('#add-events-form');
	form.submit(function (event) {
		event.preventDefault();
		var data = {};
		form.find('input[id]').each(function (index, el) {
			data[$(this).attr('name')] = $(this).val();
		});
		$.ajax({
			url: form.attr('action'),
			type: 'POST',
			dataType: 'json',
			data: JSON.stringify(data),
		})
		.done(function () {
			var modal = $('#add-events-modal');
			modal.modal('hide');
			calendar.view();
		})
		.fail(function() {
			console.log("error");
		})
		
	});

	$('#add-events-modal').on('hidden.bs.modal', function (e) {
		form.find('input').each(function (index, el) {
			$(this).val('');
		});
	})

}(jQuery));
