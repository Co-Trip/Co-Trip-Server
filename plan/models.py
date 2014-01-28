from django.db import models
from django import forms
# Create your models here.
from django.forms import ModelForm
from django.contrib.admin import widgets
from django.forms.extras import SelectDateWidget
from django.forms.widgets import CheckboxSelectMultiple, Select
from traveller.models import Traveller
from cities_light.models import City


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
    participants = models.ManyToManyField('traveller.Traveller', related_name='participate_plan_set')
    creator = models.ForeignKey('traveller.Traveller', related_name='create_plan_set')
    is_public = models.BooleanField()
    participants_can_edit = models.BooleanField()

    def __unicode__(self):
        return u'%s' % (self.title)

    class Meta:
        permissions = (
            ('view_plan', 'View Plan'),
            ('edit_plan', 'Edit Plan'),
        )






class PlanForm(ModelForm):


    def __init__(self, current_user, *args, **kwargs):
        #current_user
        super(PlanForm, self).__init__(*args, **kwargs)
        self.fields['participants'].queryset = self.fields['participants'].queryset.exclude(id=current_user.id)

    participants = forms.ModelMultipleChoiceField(queryset=Traveller.objects.exclude())
    home_city = forms.ModelChoiceField(queryset=City.objects.filter(country='48').all())
    destination_city = forms.ModelMultipleChoiceField(queryset=City.objects.filter(country='48').all())
    class Meta:
        model = Plan
        fields = ['title', 'home_city', 'destination_city', 'leaving_date', 'leaving_transportation', 'return_date',
                  'return_transportation', 'participants_number', 'is_public', 'participants', 'participants_can_edit']

        widgets = {
        'leaving_date': SelectDateWidget(required=True),
        'return_date': SelectDateWidget(required=True),
        'leaving_transportation': Select(),
        'return_transportation': Select(),

        }


#
# class PlanForm(forms.Form):
#     #create_time = forms.DateTimeField('create time')
#     title = forms.CharField(max_length=30)
#     #leaving_date = forms.DateTimeField('start date')
#     #return_date = forms.DateTimeField('back date')
#     leaving_transportation = forms.CharField(max_length=15)
#     return_transportation = forms.CharField(max_length=15)
#     participants_number = forms.IntegerField()