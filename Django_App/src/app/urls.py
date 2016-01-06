from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

#URLs are stored as a tuple.

# Working on finding all of the necessary URLs we
# will need in the end.  Make mention if you see
# any that need to be added.

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'joins.views.home', name='home'), #Home URL
    url(r'^jakeisdaman/', include(admin.site.urls)), #URL for the admin panel
)
