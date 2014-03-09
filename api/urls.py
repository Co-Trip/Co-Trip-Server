from friendship.api import FollowerResource, FollowingResource
from tastypie.api import Api
from plan.api import PlanResource
from traveller.api import TravellerResource
from notifications.api import NoficationResource
from django.conf.urls import patterns, url, include

__author__ = 'danielqiu'


v1_api = Api(api_name='v1')
v1_api.register(PlanResource())
v1_api.register(TravellerResource())
v1_api.register(NoficationResource())
v1_api.register(FollowerResource())
v1_api.register(FollowingResource())

urlpatterns = patterns('',
                        url(r'^', include(v1_api.urls)),
                        #url(r'^/v1/plan/add', include(v1_api.urls)),

)
