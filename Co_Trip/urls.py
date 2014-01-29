from django.conf.urls import patterns, include, url

from django.contrib import admin
from Co_Trip.views import AboutView


admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^$', 'Co_Trip.views.home', name='home'),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^accounts/', include('registration.backends.default.urls')),
                       url(r'^plan/', include('plan.urls')),
                       url(r'^about/', AboutView.as_view(), name="about"),

)
