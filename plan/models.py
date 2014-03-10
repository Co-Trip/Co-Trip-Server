from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db import models
from django import forms
from django.db.models.query import EmptyQuerySet
from django.forms import ModelForm
from django.forms.extras import SelectDateWidget
from django.forms.widgets import Select, SelectMultiple
from Co_Trip import settings
from ajax_select.fields import AutoCompleteSelectField
from cached_modelforms import CachedModelChoiceField, CachedModelMultipleChoiceField
from cities_light.contrib.ajax_selects_lookups import CityLookup
from friendship.models import Follow
from traveller.models import Traveller
from cities_light.models import City
from ajax_select import make_ajax_field
from bootstrap3_datetime.widgets import DateTimePicker


class Plan(models.Model):
    TRANSPORTATION_CHOICES = (
        ('plane', 'Plane'),
        ('train', 'Train'),
        ('bus', 'Bus'),
        ('other', 'Other'),

    )

    create_time = models.DateTimeField('create time')
    title = models.CharField(max_length=30)
    home_city = models.ForeignKey('cities_light.City', related_name='home_city_plan_set')
    destination_city = models.ManyToManyField('cities_light.City', related_name='destination_city_set')
    leaving_date = models.DateTimeField('leave date')
    return_date = models.DateTimeField('return date')
    leaving_transportation = models.CharField(max_length=15, choices=TRANSPORTATION_CHOICES)
    return_transportation = models.CharField(max_length=15, choices=TRANSPORTATION_CHOICES)
    participants_number = models.IntegerField()
    participants = models.ManyToManyField('traveller.Traveller', related_name='participate_plan_set', blank=True)
    creator = models.ForeignKey('traveller.Traveller', related_name='create_plan_set')
    is_public = models.BooleanField()
    participants_can_edit = models.BooleanField()
    #days = models.IntegerField()




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


class Site(models.Model):
    #start_time = models.TimeField()
    #end_time = models.TimeField()
    daily_plan = models.ForeignKey('plan.DailyPlan', related_name='daily_site_set', null=True)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    spend = models.IntegerField()
    description = models.CharField(max_length=1024)
    up_voters = models.ManyToManyField('traveller.Traveller', related_name='up_voting_plan_set')
    down_voters = models.ManyToManyField('traveller.Traveller', related_name='down_voting_plan_set')

class Meal(models.Model):
    MEAL_TYPE_CHOICE = (
        ('breakfast', 'Breakfast'),
        ('lunch', 'Lunch'),
        ('supper', 'Supper'),
        ('other', 'Other'),
    )
    meal_type = models.CharField(max_length=15, choices=MEAL_TYPE_CHOICE)
    daily_plan = models.ForeignKey('plan.DailyPlan', related_name='meal_set')

class SiteImage(models.Model):
    image = models.ImageField(upload_to=settings.MEDIA_ROOT)
    site = models.ForeignKey('plan.Site', related_name='site_image_set')



class DailyPlan(models.Model):

    TRANSPORTATION_CHOICES = (
        ('plane', 'Plane'),
        ('train', 'Train'),
        ('bus', 'Bus'),
        ('other', 'Other'),

    )

    day_number = models.IntegerField()
    hotel = models.CharField(max_length=20)
    transportation = models.CharField(max_length=15, choices=TRANSPORTATION_CHOICES)
    primary_plan = models.ForeignKey('plan.Plan', related_name='daily_plan_set')


    class Meta:
        permissions = (
            ('view_plan_permission', 'View Plan'),
            ('edit_plan_permission', 'Edit Plan'),
        )



class PlanForm(ModelForm):

    def __init__(self, current_user, *args, **kwargs):
        # daily_plan_set = kwargs.pop('daily_plan_set')
        super(PlanForm, self).__init__(*args, **kwargs)


        followers = Follow.objects.followers(current_user)
        followings = Follow.objects.following(current_user)
        particioants_choice_list = list(set(followers+followings))



        self.fields['participants'] = CachedModelMultipleChoiceField(particioants_choice_list)

        self.fields['home_city'].initial = current_user.profile.city


    participants = CachedModelMultipleChoiceField(widget=SelectMultiple(attrs={'class': 'form-control'}))
    home_city = forms.ModelChoiceField(queryset=City.objects.filter(country='48').all(),
                                       widget=Select(attrs={'class': 'form-control'}),
                                       empty_label="choose your home city")
    destination_city = forms.ModelMultipleChoiceField(
        queryset=City.objects.filter(country='48').all(),
        widget=SelectMultiple(attrs={'class': 'form-control'}))



    class Meta:
        model = Plan
        fields = ['title', 'home_city',
                  'destination_city', 'leaving_date', 'leaving_transportation', 'return_date',
                  'return_transportation', 'is_public', 'participants', 'participants_can_edit']

        widgets = {
            'leaving_date':  SelectDateWidget(),
            'return_date':  SelectDateWidget(),
            'leaving_transportation': Select(attrs={'class': 'form-control'}),
            'return_transportation': Select(attrs={'class': 'form-control'}),

        }

class DailyPlanForm(ModelForm):

    class Meta:
        model = DailyPlan
        fields = ['hotel', 'transportation']


