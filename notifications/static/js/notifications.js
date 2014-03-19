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
    var _itemTimeSince = data['timesince'];
    var _itemID = data['id'];
    var _slug = data['slug'];
    var _itemURL = data['data']['url'];
    var _actor = data['actor'];
    var _actorURL = data['actorURL'];
    var _hasDeleteButton = true;

    if (_itemURL !== undefined) {
        _verb.replace('新私信', '<a href="' + _itemURL + '">新私信</a>');
    };

    this.tojQueryObject = function () {
        var notificationItem = $('<li class="media CT-notification-item"></li>');

        // Close button
        var deleteButton = '<a class="close" data-dismiss="alert" href="#" aria-hidden="true">&times;</a>';

        // Media body
        var mediaBody = $('<div class="media-body CT-notification-item-content"></div>');
        var mediaHeading = '<h4 class="media-heading"><a href="' + _actorURL + '">' + _actor + '</a>' + _verb + ' <small><i>' + _itemTimeSince + '</i></small></h4>';

        mediaBody.append(mediaHeading);

        if (_hasDeleteButton) {
            notificationItem.append(deleteButton);

            // Mark as read
            notificationItem.bind('close.bs.alert', function () {
                $.get('/notifications/mark-as-read/' + _slug + '/');
            })
        };
        notificationItem.append(mediaBody);
        notificationItem.hide();

        return notificationItem;
    };

    this.isUnread = function () {
        return _isUnread;
    };

    this.removeDeleteButton = function () {
        _hasDeleteButton = false;
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

    // load unread list
    $.getJSON('/api/v1/unread_notification/', 
        {format: 'json'}, 
        function(json, textStatus) {
            var obj = json["objects"];
            var unreadNumber = 0;
            $('#unread-list').empty();
            $('#unread-badge').empty();
            for (var i = 0; i < obj.length; i++) {
                var item = new Notifis(obj[i]);
                if (item.isUnread()) {
                    unreadNumber ++;
                }
                var $item = item.tojQueryObject();
                $('#unread-list').append($item);
                $item.fadeIn();
            }
            if (unreadNumber != 0) {
                $('#unread-badge').text(unreadNumber);
            } else {
                $('#unread-badge').empty();
            }
    });
});

$('a[href="#unread"]').on('show.bs.tab', function (e) {
    $.getJSON('/api/v1/unread_notification/', 
        {format: 'json'}, 
        function(json, textStatus) {
            var obj = json["objects"];
            var unreadNumber = 0;
            $('#unread-list').empty();
            $('#unread-badge').empty();
            for (var i = 0; i < obj.length; i++) {
                var item = new Notifis(obj[i]);
                if (item.isUnread()) {
                    unreadNumber ++;
                }
                var $item = item.tojQueryObject();
                $('#unread-list').append($item);
                $item.fadeIn();
            }
            if (unreadNumber != 0) {
                $('#unread-badge').text(unreadNumber);
            } else {
                $('#unread-badge').empty();
            }
    });
});
$('a[href="#all"]').on('show.bs.tab', function (e) {
    $.getJSON('/api/v1/all_notification/', 
        {format: 'json'}, 
        function(json, textStatus) {
            var obj = json["objects"];
            $('#all-list').empty();
            for (var i = 0; i < obj.length; i++) {
                var item = new Notifis(obj[i]);
                item.removeDeleteButton();
                var $item = item.tojQueryObject();
                $('#all-list').append($item);
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
