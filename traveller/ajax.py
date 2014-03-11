# -*- coding: utf-8 -*
from django.shortcuts import render, redirect
from friendship.exceptions import AlreadyExistsError
from friendship.models import Follow
from friendship.views import user_model
from notifications import notify

__author__ = 'danielqiu'

from django.contrib.auth.decorators import login_required
import json

__author__ = 'danielqiu'


from dajaxice.decorators import dajaxice_register


@dajaxice_register
def sayhello(request):
    return json.dumps({'message':'Hello World'})



@login_required
def follower_add(request, followee_username, template_name='friendship/follow/add.html'):
    """ Create a following relationship """
    ctx = {'followee_username': followee_username}

    if request.method == 'POST':
        followee = user_model.objects.get(username=followee_username)
        follower = request.user
        try:
            Follow.objects.add_follower(follower, followee)
            notify.send(follower, recipient=followee, verb=u'关注了你',)
        except AlreadyExistsError as e:
            ctx['errors'] = ["%s" % e]
        else:
            return redirect('friendship_following', username=follower.username)

    return render(request, template_name, ctx)