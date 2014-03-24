# -*- coding: utf-8 -*
import json

from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.http import HttpResponse
from notifications import notify

try:
    from django.contrib.auth import get_user_model
    user_model = get_user_model()
except ImportError:
    from django.contrib.auth.models import User
    user_model = User

from django.shortcuts import render, get_object_or_404, redirect

from friendship.exceptions import AlreadyExistsError
from friendship.models import Follow

get_friendship_context_object_name = lambda: getattr(settings, 'FRIENDSHIP_CONTEXT_OBJECT_NAME', 'user')
get_friendship_context_object_list_name = lambda: getattr(settings, 'FRIENDSHIP_CONTEXT_OBJECT_LIST_NAME', 'users')





def followers(request, username, template_name='friendship/follow/followers_list.html'):
    """ List this user's followers """
    user = get_object_or_404(user_model, username=username)
    followers = Follow.objects.followers(user)

    return render(request, template_name, {get_friendship_context_object_name(): user, 'followers': followers})


def following(request, username, template_name='friendship/follow/following_list.html'):
    """  List who this user follows """
    user = get_object_or_404(user_model, username=username)
    following = Follow.objects.following(user)

    return render(request, template_name, {get_friendship_context_object_name(): user, 'following': following})


@login_required
def follower_add(request, followee_username, template_name='friendship/follow/add.html'):
    """ Create a following relationship """
    ctx = {'followee_username': followee_username}

    if request.method == 'GET':
        followee = user_model.objects.get(username=followee_username)
        follower = request.user
        try:
            Follow.objects.add_follower(follower, followee)
            notify.send(follower, recipient=followee, verb=u'关注了你',)
        except AlreadyExistsError as e:
            ctx['errors'] = ["%s" % e]
            to_json = {"success": 0}
            return HttpResponse(json.dumps(to_json), mimetype='application/json')
        to_json = {"success": 1}
        return HttpResponse(json.dumps(to_json), mimetype='application/json')

    return render(request, template_name, ctx)


@login_required
def follower_remove(request, followee_username, template_name='friendship/follow/remove.html'):
    """ Remove a following relationship """
    if request.method == 'GET':
        followee = user_model.objects.get(username=followee_username)
        follower = request.user
        Follow.objects.remove_follower(follower, followee)
        to_json = {"success": 1}
        return HttpResponse(json.dumps(to_json), mimetype='application/json')

    return render(request, template_name, {'followee_username': followee_username})


def all_users(request, template_name="friendship/user_actions.html"):
    users = user_model.objects.all()

    return render(request, template_name, {get_friendship_context_object_list_name(): users})

def is_following(request, followee_username):
    target_user = get_object_or_404(user_model, username=followee_username)
    following = Follow.objects.following(request.user)
    if target_user.profile  in following:
        to_json = {"result": 1}
        return HttpResponse(json.dumps(to_json), mimetype='application/json')
    else:
        to_json = {"result": 0}
        return HttpResponse(json.dumps(to_json), mimetype='application/json')