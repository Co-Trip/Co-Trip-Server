from friendship.models import Follow
from tastypie.resources import ModelResource
from tastypie.serializers import Serializer

__author__ = 'danielqiu'



class FollowerResource(ModelResource):
    class Meta:
        queryset = Follow.objects.all()
        resource_name = 'follower'
        serializer = Serializer()
        limit = 10

    def dehydrate(self, bundle):
        bundle.data['username'] = bundle.obj.follower.username

        return bundle


class FollowingResource(ModelResource):
    class Meta:
        queryset = Follow.objects.all()
        resource_name = 'following'
        serializer = Serializer()
        limit = 10

    def dehydrate(self, bundle):


        return bundle
