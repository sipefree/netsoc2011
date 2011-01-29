from django.conf.urls.defaults import *
from tagging.views import tagged_object_list
import netsoc2011
import models
info_dict = {
	'queryset': models.Entry.objects.filter(status=1),
	'date_field': 'pub_date',
}

urlpatterns = patterns('',
	(r'search', 'news.views.news_search'),
	(r'(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<slug>[-\w]+)/$', 'news.views.news_detail'),
	#(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<slug>[-\w]+)/$', 'object_detail', dict(info_dict, month_format= '%m', template_name='news/list.html')),
	#(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/$', 'archive_day', dict(info_dict, month_format= '%m', template_name='news/list.html')),
	#(r'^(?P<year>\d{4})/(?P<month>\d{2})/$', 'archive_month', dict(info_dict, month_format= '%m', template_name='news/list.html')),
	#(r'^(?P<year>\d{4})/$', 'archive_year', dict(info_dict, template_name='news/list.html')),
	(r'^$', 'news.views.news_archive_index')
)