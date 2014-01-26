from traveller.views import *
from django.contrib.auth.decorators import login_required

__author__ = 'danielqiu'

from django.conf.urls import patterns, url, include
from plan import views


urlpatterns = patterns('',

                           url(r'^$',login_required(ProfileView.as_view()), name='profile'),
                           url(r'^plan/detail/(?P<plan_id>\d+)/$', login_required(PlanDetailView.as_view()), name="detail"),
                           url(r'^edit$', login_required(ProfileEditView.as_view()), name="detail"),

)