from django.contrib.auth import admin
from traveller.models import Traveller, TravellerAdmin
from traveller.views import *
from django.contrib.auth.decorators import login_required
from . import views
from upload_avatar.app_settings import UPLOAD_AVATAR_URL_PREFIX_CROPPED, UPLOAD_AVATAR_URL_PREFIX_ORIGINAL

__author__ = 'danielqiu'

from django.conf.urls import patterns, url, include

urlpatterns = patterns('',

                       url(r'^$', login_required(ProfileView.as_view()), name='profile'),
                       url(r'^edit/$', login_required(ProfileEditView.as_view()), name="edit"),
                       url(r'^traveller_list/$', login_required(ProfileListView.as_view()), name="all_list"),
                       url(r'^(?P<profile_id>\d+)/$', login_required(ProfileView.as_view()), name="profile_detail"),
                       url(r'^upload/$', upload, name="upload_avatar"),
                       url(r'%s(?P<filename>.+)/?$' % UPLOAD_AVATAR_URL_PREFIX_ORIGINAL,
                           views.get_upload_images
                       ),
                       url(r'^%s(?P<filename>.+)/?$' % UPLOAD_AVATAR_URL_PREFIX_CROPPED,
                           views.get_avatar
                       ),
                       url(r'^search/$', search, name='search_user'),

)
