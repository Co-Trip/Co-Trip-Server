from django.contrib.auth.decorators import login_required
from django.views.generic import RedirectView


__author__ = 'danielqiu'

from django.conf.urls import patterns, url, include
from plan.views import *




urlpatterns = patterns('',

                       url(r'^explore/$', explore, name='explore'),
                       # url(r'^explore/(?P<plan_id>\d+)/$', detail, name='detail'),
                       # url(r'^explore/(?P<plan_id>\d+)/edit$',
                       #     permission_required_or_403('plan.edit_plan_permission', (Plan, 'id', 'plan_id'))(
                       #         PlanEditView.as_view()), name='detail'),
                       # url(r'^explore/(?P<plan_id>\d+)/edit/success$', edit_success, name='success'),
                       # url(r'^create/success/$', create_success, name='success'),
                       url(r'^detail/(?P<plan_id>\d+)/$', detail, name='plan_detail'),
                       #url(r'^create/daily_plan_create/$', DailyPlanCreateView.as_view(), name='daily_plan_creation')

                       url(r'create/$', RedirectView.as_view(url='step1/'),name='create'),
                       url(r'^create/step1/$', login_required(PlanCreateStep1View.as_view()), name='create_step1'),
                       url(r'^edit/(?P<plan_id>\d+)/$', permission_required_or_403('plan.edit_plan_permission', (Plan, 'id', 'plan_id'))
                        (PlanCreateStep2View.as_view()), name='create_step2'),

                       url(r'^edit/(?P<plan_id>\d+)/events/', login_required(PlanEventView.as_view()), name='events'),
                       url(r'^detail/(?P<plan_id>\d+)/events/', login_required(PlanEventView.as_view()), name='events')

)
