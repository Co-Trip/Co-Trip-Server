__author__ = 'danielqiu'
from tastypie.resources import ModelResource
from models import Traveller
from tastypie.serializers import Serializer

class TravellerResource(ModelResource):
    class Meta:
        queryset = Traveller.objects.all()
        resource_name = 'traveller'
        serializer = Serializer()