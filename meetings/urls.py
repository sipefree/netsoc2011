from django.conf.urls.defaults import *
from tagging.views import tagged_object_list
import netsoc2011
import models

urlpatterns = patterns('',
	(r'search', 'meetings.views.meetings_search'),
	(r'(?P<id>\d+)/$', 'meetings.views.meeting_detail'),
	(r'^$', 'meetings.views.meetings_archive_index')
)