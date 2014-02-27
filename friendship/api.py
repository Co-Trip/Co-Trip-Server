__author__ = 'danielqiu'

from friendship.models import Friend, FriendshipRequest
from tastypie.resources import ModelResource
from tastypie.serializers import Serializer

class FriendResource(ModelResource):
    class Meta:
        queryset = Friend.objects.all()
        resource_name = 'friend'
        serializer = Serializer()

class FriendshipRequestResource(ModelResource):
    class Meta:
        queryset = FriendshipRequest.objects.all()
        resource_name = 'friend_request'
        serializer = Serializer()