from tastypie.contrib.contenttypes import fields
from tastypie.fields import OneToManyField
from tastypie.resources import ModelResource
from city.models import City, Province
from tastypie.serializers import Serializer



class ProvinceResource(ModelResource):

    class Meta:
        queryset = Province.objects.all()
        resource_name = 'province'
        serializer = Serializer()
        limit = 40

    def dehydrate(self, bundle):
        city = []
        for c in bundle.obj.city_set.all():
            city.append(c)

        bundle.data['city'] = city

        return bundle

