/**
 * 
 * @authors Tom Hu (h1994st@gmail.com)
 * @date    2014-02-26 17:11:38
 * @version 1.0
 */
if (typeof jQuery === 'undefined') { throw new Error('requires jQuery') }

/**
 * 'data' is Json Format
 */
var Notifis = function (data) {
    var _isUnread = data['unread'];
    var _verb = data['verb'];
    var _itemTime = data['timestamp'];
    var _itemID = data['id'];
    var _itemURL = data['data']['url'];
    var _actor = data['actor'];
    var _actorURL = data['actorURL'];

    this.tojQueryObject = function () {
        var notificationItem = $('<li class="media CT-notification-item"></li>');

        // Close button
        var deleteButton = '<a class="close" data-dismiss="alert" href="#" aria-hidden="true">&times;</a>';

        // Media body
        var mediaBody = $('<div class="media-body CT-notification-item-content"></div>');
        var mediaHeading = '<h4 class="media-heading"><a href="' + _actorURL + '">' + _actor + '</a>' + _verb + '</h4>';

        mediaBody.append(mediaHeading);

        notificationItem.append(deleteButton);
        notificationItem.append(mediaBody);
        notificationItem.hide();

        return notificationItem;
    };

    this.isUnread = function () {
        return _isUnread;
    };
};

$(document).ready(function() {
    $('button[data-toggle="clear_notification"]').click(function(event) {
        $('.CT-notification-list').empty();
        var unreadNumber = parseInt($('#unread-badge').text());
        $('#unread-badge').empty();
        var readNumber = parseInt($('#read-badge').text());
        $('#read-badge').text(readNumber + unreadNumber);
        $('#notification-circle').removeClass('notification-unread');
    });

    // load inbox list
    $.getJSON('/api/v1/received_message/', 
        {format: 'json'}, 
        function(json, textStatus) {
            var obj = json["objects"];
            var unreadNumber = 0;
            $('#inbox-list').empty();
            for (var i = 0; i < obj.length; i++) {
                var item = new Message(obj[i], false);
                if (item.isUnread()) {
                    unreadNumber ++;
                }
                var $item = item.tojQueryObject();
                $('#inbox-list').append($item);
                $item.fadeIn();
            }
            if (unreadNumber != 0) {
                $('#inbox-badge').text(unreadNumber);
            }
    });
});

$('a[href="#inbox"]').on('show.bs.tab', function (e) {
    $.getJSON('/api/v1/received_message/', 
        {format: 'json'}, 
        function(json, textStatus) {
            var obj = json["objects"];
            var unreadNumber = 0;
            $('#inbox-list').empty();
            $('#inbox-badge').empty();
            for (var i = 0; i < obj.length; i++) {
                var item = new Message(obj[i], false);
                if (item.isUnread()) {
                    unreadNumber ++;
                }
                var $item = item.tojQueryObject();
                $('#inbox-list').append($item);
                $item.fadeIn();
            }
            if (unreadNumber != 0) {
                $('#inbox-badge').text(unreadNumber);
            }
    });
});
$('a[href="#sent"]').on('show.bs.tab', function (e) {
    $.getJSON('/api/v1/sent_message/', 
        {format: 'json'}, 
        function(json, textStatus) {
            var obj = json["objects"];
            $('#sent-list').empty();
            for (var i = 0; i < obj.length; i++) {
                var item = new Message(obj[i]);
                var $item = item.tojQueryObject();
                $('#sent-list').append($item);
                $item.fadeIn();
            }
    });
});
$('a[href="#trash"]').on('show.bs.tab', function (e) {
    $.getJSON('/api/v1/deleted_message/', 
        {format: 'json'}, 
        function(json, textStatus) {
            var obj = json["objects"];
            $('#trash-list').empty();
            for (var i = 0; i < obj.length; i++) {
                var item = new Message(obj[i]);
                var $item = item.tojQueryObject();
                $('#trash-list').append($item);
                $item.fadeIn();
            }
    });
});

/**
 * Always focus on first tab
 */
$('#main-tabs a[data-toggle="tab"]').on('shown.bs.tab', function (e) {
    var selector = $(this).attr('href') + ' .CT-sidetabbar a[data-toggle="pill"]:first';
    $(selector).tab('show');
    $('button[data-toggle="clear_notification"]').fadeIn(100);
    $('button[data-toggle="clear_notification"]').removeClass('disabled');
});

/**
 * When the first tab is showing, button 'Mark all as read' also shows
 */
$('.CT-sidetabbar li.active a[data-toggle="pill"]').on('shown.bs.tab', function (e) {
    $('button[data-toggle="clear_notification"]').fadeIn(100);
    $('button[data-toggle="clear_notification"]').removeClass('disabled');
});
$('.CT-sidetabbar li:not("li.active") a[data-toggle="pill"]').on('shown.bs.tab', function (e) {
    $('button[data-toggle="clear_notification"]').fadeOut(100);
    $('button[data-toggle="clear_notification"]').addClass('disabled');
});
