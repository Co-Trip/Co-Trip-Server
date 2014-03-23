from django.forms import ModelForm, SelectMultiple, Select, TimeInput, SplitDateTimeWidget, CheckboxSelectMultiple
from django.forms.extras import SelectDateWidget
from cached_modelforms import CachedModelMultipleChoiceField
from city.models import City
from friendship.models import Follow
from django import forms
from plan.models import Plan,Event

__author__ = 'danielqiu'


class PlanForm(ModelForm):

    def __init__(self, current_user, *args, **kwargs):

        super(PlanForm, self).__init__(*args, **kwargs)


        followers = Follow.objects.followers(current_user)
        followings = Follow.objects.following(current_user)
        participants_choice_list = list(set(followers+followings))



        # self.fields['participants'] = CachedModelMultipleChoiceField(participants_choice_list,
        #                                                              required=False,
        #                                                              widget=
        #                                                              CheckboxSelectMultiple(attrs={'class': 'form-control','class':"CT-item-checkbox",'form':"plan-form"}),)

        #self.fields['home_city'].initial = current_user.profile.city

    # home_city = forms.ModelChoiceField(queryset=City.objects.all(),
    #                                    widget=Select(attrs={'class': 'form-control'}),
    #                                    empty_label="choose your home city")
    destination_city = forms.ModelMultipleChoiceField(
        queryset=City.objects.all(),
        widget=SelectMultiple(attrs={'class': 'form-control'}))



    class Meta:
        model = Plan
        fields = ['title', #'home_city',
                  'destination_city', 'leaving_date', 'leaving_transportation', 'return_date',
                  'return_transportation', 'is_public', 'participants_can_edit']

        widgets = {
            'leaving_date':  SelectDateWidget(),
            'return_date':  SelectDateWidget(),
            'leaving_transportation': Select(attrs={'class': 'form-control'}),
            'return_transportation': Select(attrs={'class': 'form-control'}),
        }

#
# class EventForm(ModelForm):
#
#     class Meta:
#         model = Event
#         exclude = ['main_plan']
#         widgets = {
#             'start_time':SplitDateTimeWidget,
#             'end_time':TimeInput
#
#         }