from friendship.models import Follow
from tastypie.resources import ModelResource
from tastypie.serializers import Serializer

__author__ = 'danielqiu'



class FollowerResource(ModelResource):
    class Meta:
        queryset = Follow.objects.all()
        resource_name = 'follower'
        serializer = Serializer()

class FollowingResource(ModelResource):
    class Meta:
        queryset = Follow.objects.all()
        resource_name = 'Following'
        serializer = Serializer()