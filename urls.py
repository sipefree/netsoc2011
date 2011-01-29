from django.conf.urls.defaults import *
from django.contrib import admin
import netsoc2011
from feeds import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^netsoc2011/', include('netsoc2011.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
	(r'^pages/(?P<slug>[-\w]+)/$', 'pages.views.detail'),
	(r'^meetings/', include('netsoc2011.meetings.urls')),
	(r'^news/', include('netsoc2011.news.urls')),
	(r'^events/', include('netsoc2011.events.urls')),
	(r'^tutorials/', include('netsoc2011.tutorials.urls')),
	(r'^tags/(?P<slug>[a-zA-Z0-9_.-]+)/$', 'netsoc2011.tagviews.tag_detail'),
	(r'^images/(?P<path>.*)$', 'django.views.static.serve', {'document_root': '/Users/theorie/Development/netsoc2011/media/images'}),
	(r'^static_files/(?P<path>.*)$', 'django.views.static.serve', {'document_root': '/Users/theorie/Development/netsoc2011/static_files'}),
	(r'^js/(?P<path>.*)$', 'django.views.static.serve', {'document_root': '/Users/theorie/Development/netsoc2011/media/js'}),
	(r'^css/(?P<path>.*)$', 'django.views.static.serve', {'document_root': '/Users/theorie/Development/netsoc2011/media/css'}),
	(r'^feeds/news/$', LatestNewsFeed()),
	(r'^feeds/events/$', LatestEventsFeed()),
	(r'^$', 'pages.views.site_index'),
)