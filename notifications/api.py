__author__ = 'danielqiu'
from tastypie.resources import ModelResource
from models import Notification
from tastypie.serializers import Serializer

class NoficationResource(ModelResource):
    class Meta:
        queryset = Notification.objects.all()
        resource_name = 'notification'
        #excludes = ['home_city','destination_city','participants','creator']
        serializer = Serializer()
