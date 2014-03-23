from django.db import models

# Create your models here.
class City(models.Model):
    city_name = models.CharField(max_length=32)
    province = models.ForeignKey('city.Province', related_name='city_set')
    city_sort = models.IntegerField()

    def __unicode__(self):
        return self.city_name

class Province(models.Model):
    province_name = models.CharField(max_length=16)
    province_sort = models.IntegerField()
    def __unicode__(self):
        return self.province_name



