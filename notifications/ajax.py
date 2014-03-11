import json

__author__ = 'danielqiu'
from dajaxice.decorators import dajaxice_register


@dajaxice_register
def check_unread(request):
    print request.user.notifications.unread()
    if len(request.user.notifications.unread()):
        response_data = {'has_unread':False}
    else:
        response_data = {'has_unread':True}
    return json.dumps(response_data)
