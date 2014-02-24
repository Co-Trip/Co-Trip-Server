__author__ = 'danielqiu'
from tastypie.resources import ModelResource
from models import Plan
from tastypie.serializers import Serializer

class PlanResource(ModelResource):
    class Meta:
        queryset = Plan.objects.all()
        resource_name = 'plan'
        excludes = ['home_city','destination_city','participants','creator']
        serializer = Serializer()
