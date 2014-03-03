from django.conf.urls import patterns, include, url
from ajax_select import urls as ajax_select_urls
from django.contrib import admin
from Co_Trip.views import AboutView

import notifications


admin.autodiscover()



urlpatterns = patterns('',
                       url(r'^$', 'Co_Trip.views.home', name='home'),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^accounts/', include('registration.backends.default.urls')),
                       url(r'^plan/', include('plan.urls')),
                       url(r'^about/', AboutView.as_view(), name="about"),
                       url(r'^lookups/', include(ajax_select_urls)),
                       url(r'^inbox/notifications/', include(notifications.urls)),
                       url(r'^api/', include('api.urls')),
                       url(r'^friend/', include('friendship.urls')),
                       url(r'^comments/', include('django_comments.urls')),
                       url(r'', include('upload_avatar.urls')),
)


from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns += staticfiles_urlpatterns()
