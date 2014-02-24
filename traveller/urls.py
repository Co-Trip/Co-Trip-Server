from django.contrib.auth import admin
from traveller.models import Traveller, TravellerAdmin
from traveller.views import *
from django.contrib.auth.decorators import login_required

__author__ = 'danielqiu'

from django.conf.urls import patterns, url, include
from plan import views


urlpatterns = patterns('',

                           url(r'^$',login_required(ProfileView.as_view()), name='profile'),
                           url(r'^plan/detail/(?P<plan_id>\d+)/$',
                               permission_required_or_403('plan.view_plan', (Plan, 'id', 'plan_id'))(PlanDetailView.as_view()), name="detail"),
                           url(r'^edit/$', login_required(ProfileEditView.as_view()), name="edit"),
                           url(r'^traveller_list/$', login_required(ProfileListView.as_view()), name="all_list"),
                           url(r'^(?P<profile_id>\d+)/$',login_required(ProfileView.as_view()), name="profile detail"),
                           url(r'^(?P<profile_id>\d+)/add_friend$',login_required(AddFriend.as_view()), name="add_friend"),

)
