/**
 * 
 * @authors Tom Hu (h1994st@gmail.com)
 * @date    2014-03-21 21:56:46
 * @version 1.0
 */

(function ($) {
    $(document).ready(function() {
        $button = $('#follow-or-not');
        $.get('/follow/follower/is_following/' + $button.data('username'), function (data) {
            if (data['result'] === 1) {
                $button.text('取消关注');
                $button.data('action', 'remove');
            } else {
                $button.text('关注');
                $button.data('action', 'add');
            }
        });
        $button.click(function (event) {
            $.get('/follow/follower/' + $(this).data('action') + '/' + $(this).data('username'), function (data) {
                alert(JSON.stringify(data));
            });
        });
    });
})(jQuery)