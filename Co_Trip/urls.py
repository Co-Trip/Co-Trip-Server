from django.conf.urls import patterns, include, url
from ajax_select import urls as ajax_select_urls
from django.contrib import admin
from Co_Trip.views import AboutView
import autocomplete_light

import notifications
from dajaxice.core import dajaxice_autodiscover, dajaxice_config
from traveller.models import Traveller


autocomplete_light.autodiscover()

admin.autodiscover()

dajaxice_autodiscover()

urlpatterns = patterns('',
                       url(r'^$', 'Co_Trip.views.home', name='home'),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^accounts/', include('registration.backends.default.urls')),
                       url(r'^plan/', include('plan.urls')),
                       url(r'^about/', AboutView.as_view(), name="about"),
                       url(r'^lookups/', include(ajax_select_urls)),
                       url(r'^notifications/', include(notifications.urls)),
                       url(r'^api/', include('api.urls')),
                       url(r'^follow/', include('friendship.urls')),
                       url(r'^comments/', include('django_comments.urls')),
                       url(r'', include('upload_avatar.urls')),
                       url(dajaxice_config.dajaxice_url, include('dajaxice.urls')),
                       url(r'^autocomplete/', include('autocomplete_light.urls')),
                       url(r'^messages/', include('django_messages.urls')),
                       url('', include('social.apps.django_app.urls', namespace='social'))
)

# autocomplete_light.register(Traveller, TravellerAutocomplete)

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns += staticfiles_urlpatterns()
