 # -*- coding: utf-8 -*
from django.core.urlresolvers import reverse
from django.db import models
from Co_Trip import settings



class Plan(models.Model):
    TRANSPORTATION_CHOICES = (
        ('plane', '飞机'),
        ('train', '火车'),
        ('bus', '客运'),
        ('other', '其他'),

    )

    create_time = models.DateTimeField('create time')
    title = models.CharField(max_length=30)
    home_city = models.ForeignKey('city.City', related_name='home_city_plan_set', null=True)
    destination_city = models.ManyToManyField('city.City', related_name='destination_city_set')
    leaving_date = models.DateTimeField('leave date')
    return_date = models.DateTimeField('return date')
    leaving_transportation = models.CharField(max_length=15, choices=TRANSPORTATION_CHOICES)
    return_transportation = models.CharField(max_length=15, choices=TRANSPORTATION_CHOICES)
    participants_number = models.IntegerField()
    participants = models.ManyToManyField('traveller.Traveller',
                                          related_name='participate_plan_set', blank=True, null=True)
    creator = models.ForeignKey('traveller.Traveller', related_name='create_plan_set')
    is_public = models.BooleanField()
    participants_can_edit = models.BooleanField()


    def __unicode__(self):
        return u'%s' % self.title

    @models.permalink
    def get_absolute_url(self):
        return "/plan/%i/detail" % self.id


    def get_absolute_url(self):
        return reverse('plan_detail', kwargs={'plan_id': self.id})

    class Meta:
        permissions = (
            ('view_plan_permission', 'View Plan'),
            ('edit_plan_permission', 'Edit Plan'),
        )


class Event(models.Model):
    start_time = models.CharField(max_length=32)
    end_time = models.CharField(max_length=32)
    main_plan = models.ForeignKey('plan.Plan', related_name='event_set', null=True)
    title = models.CharField(max_length=256)
    spend = models.IntegerField()
    description = models.CharField(max_length=256)
    event_class = models.CharField(max_length=20, null=True)








# class Meal(models.Model):
#     MEAL_TYPE_CHOICE = (
#         ('breakfast', 'Breakfast'),
#         ('lunch', 'Lunch'),
#         ('supper', 'Supper'),
#         ('other', 'Other'),
#     )
#     meal_type = models.CharField(max_length=15, choices=MEAL_TYPE_CHOICE)
#     daily_plan = models.ForeignKey('plan.DailyPlan', related_name='meal_set')
#
#


# class DailyPlan(models.Model):
#
#     TRANSPORTATION_CHOICES = (
#         ('plane', 'Plane'),
#         ('train', 'Train'),
#         ('bus', 'Bus'),
#         ('other', 'Other'),
#
#     )
#
#     day_number = models.IntegerField()
#     hotel = models.CharField(max_length=20)
#     transportation = models.CharField(max_length=15, choices=TRANSPORTATION_CHOICES)
#     primary_plan = models.ForeignKey('plan.Plan', related_name='daily_plan_set')
#
#
#     class Meta:
#         permissions = (
#             ('view_plan_permission', 'View Plan'),
#             ('edit_plan_permission', 'Edit Plan'),
#         )




