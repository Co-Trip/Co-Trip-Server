from django.contrib.auth.decorators import login_required


__author__ = 'danielqiu'

from django.conf.urls import patterns, url, include
from plan.views import *




urlpatterns = patterns('',

                       url(r'^explore/$', explore, name='explore'),
                       url(r'^create/$', login_required(PlanCreateView.as_view()), name='create'),
                       url(r'^explore/(?P<plan_id>\d+)/$', detail, name='detail'),
                       url(r'^explore/(?P<plan_id>\d+)/edit$',
                           permission_required_or_403('plan.edit_plan_permission', (Plan, 'id', 'plan_id'))(
                               PlanEditView.as_view()), name='detail'),
                       url(r'^explore/(?P<plan_id>\d+)/edit/success$', edit_success, name='success'),
                       url(r'^create/success/$', create_success, name='success'),
                       url(r'^(?P<plan_id>\d+)/detail/$', detail, name='plan_detail'),


)
