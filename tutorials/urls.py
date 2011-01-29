from django.conf.urls.defaults import *
from tagging.views import tagged_object_list
import netsoc2011
import models

urlpatterns = patterns('',
	(r'search', 'tutorials.views.tutorials_search'),
	(r'(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<slug>[-\w]+)/$', 'tutorials.views.tutorial_detail'),
	#(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<slug>[-\w]+)/$', 'object_detail', dict(info_dict, month_format= '%m', template_name='news/list.html')),
	#(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/$', 'archive_day', dict(info_dict, month_format= '%m', template_name='news/list.html')),
	#(r'^(?P<year>\d{4})/(?P<month>\d{2})/$', 'archive_month', dict(info_dict, month_format= '%m', template_name='news/list.html')),
	#(r'^(?P<year>\d{4})/$', 'archive_year', dict(info_dict, template_name='news/list.html')),
	(r'^$', 'tutorials.views.tutorial_archive_index')
)