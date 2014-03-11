from django.contrib.auth.models import User

__author__ = 'danielqiu'
from tastypie.resources import ModelResource
from models import Traveller
from tastypie.serializers import Serializer

class TravellerResource(ModelResource):
    class Meta:
        queryset = Traveller.objects.all()
        resource_name = 'traveller'
        serializer = Serializer()





class UserResource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        resource_name = 'user'
        excludes = ['email', 'password', 'is_active', 'is_staff', 'is_superuser']