from traveller.api import TravellerResource

__author__ = 'danielqiu'
from tastypie.resources import ModelResource
from tastypie.authorization import Authorization
from tastypie import fields
from models import Plan
from tastypie.serializers import Serializer

class PlanResource(ModelResource):

    title = fields.CharField(attribute='title')
    creator = fields.ForeignKey(TravellerResource, 'creator')
    participants = fields.ManyToManyField(TravellerResource, 'participants')

    class Meta:
        queryset = Plan.objects.all()
        resource_name = 'plan'
        serializer = Serializer()
        authorization= Authorization()
        #fields = ['title', 'creator', 'participants']

