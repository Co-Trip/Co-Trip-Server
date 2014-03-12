/**
 * 
 * @authors Tom Hu (h1994st@gmail.com)
 * @date    2014-02-26 17:11:38
 * @version 1.0
 */
if (typeof jQuery === 'undefined') { throw new Error('requires jQuery') }

var Message = function (data) {
    var _data = data;
    var _senderName = data["senderName"];
    var _senderURL = data["senderURL"];
    var _senderAvatarImg = data["userAvatarImg"];
    var _messageURL = data["messageURL"];
    var _messageSubject = data["messageSubject"];
    var _messageBody = data["messageBody"];
    var _messageID = data["messageID"];

    this.tojQueryObject = function () {
        var messageItem = $('<li class="media CT-message-item"></li>');

        // Avatar
        var senderAvatar = '<a class="pull-left" href="' + _senderURL + '"><img src="' + _senderAvatarImg + '" alt="' + _senderName + '" class="media-object avatar"></a>';

        // Close button
        var deleteButton = '<a class="close" data-dismiss="alert" href="#" aria-hidden="true">&times;</a>';

        // Media body
        var mediaBody = $('<div class="media-body CT-message-item-content"></div>');
        var mediaHeading = '<h4 class="media-heading"><a href="' + _messageURL + '">' + _messageSubject + '</a> <small><i>From: ' + _senderName + '</i></small></h4>';
        var messageBody = '<div><small>' + _messageBody + '</small></div>';

        mediaBody.append(mediaHeading);
        mediaBody.append(messageBody);

        messageItem.append(senderAvatar);
        messageItem.append(deleteButton);
        messageItem.append(mediaBody);
        messageItem.hide();
        
        return messageItem;
    }
}

$(document).ready(function() {
    $('button[data-toggle="clear_notification"]').click(function(event) {
        $('.CT-notification-list').empty();
        var unreadNumber = parseInt($('#unread-badge').text());
        $('#unread-badge').empty();
        var readNumber = parseInt($('#read-badge').text());
        $('#read-badge').text(readNumber + unreadNumber);
        $('#notification-circle').removeClass('notification-unread');
    });
});

$('a[href="#inbox"]').on('show.bs.tab', function (e) {
    $.getJSON('http://10.0.1.23:8000/api/v1/sent_message/', 
        {format: 'json'}, 
        function(json, textStatus) {
            var obj = json["objects"];
            for (var i = 0; i < obj.length; i++) {
                var item = new Message(obj[i]);
                var $item = item.tojQueryObject();
                $('#inbox-list').append($item);
                $item.fadeIn();
            }
    });
})

