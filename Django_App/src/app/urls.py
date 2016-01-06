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

    # Possible URLs that will be needed.

    # The 'namehere' will be the part with the file name located in the views dir.

    # url(r'^about/', 'joins.views.#namehere', name='about'),
    # url(r'^event-rules/', 'joins.views.#namehere', name='event-rules'),
    # url(r'^tournaments/', 'joins.views.#namehere', name='tournaments'),
    # url(r'^gallery/', 'joins.views.#namehere', name='gallery'),
    # url(r'^sponsors/', 'joins.views.#namehere', name='sponsors'),
    # url(r'^reserve-a-seat/', 'joins.views.#namehere', name='reserve-a-seat'),
    # url(r'^my-account/', 'joins.views.#namehere', name='my-account'),
)
