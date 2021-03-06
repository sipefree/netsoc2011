from django.conf.urls.defaults import *
from tagging.views import tagged_object_list
import netsoc2011
import models
from datetime import datetime

info_dict = {
	'queryset': models.Event.objects.filter(event_date__gte=datetime.today()),
	'date_field': 'event_date',
	'allow_future': True,
	'extra_context': {
		'latest_news': netsoc2011.news.models.Entry.objects.latest()
	}
}

urlpatterns = patterns('django.views.generic.date_based',
	(r'(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<slug>[-\w]+)/$', 'object_detail', dict(info_dict, month_format= '%m', slug_field='slug', template_name='events/detail.html')),
	(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<slug>[-\w]+)/$', 'object_detail', dict(info_dict, month_format= '%m', template_name='events/list.html')),
	(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/$', 'archive_day', dict(info_dict, month_format= '%m', template_name='events/list.html')),
	(r'^(?P<year>\d{4})/(?P<month>\d{2})/$', 'archive_month', dict(info_dict, month_format= '%m', template_name='events/list.html')),
	(r'^(?P<year>\d{4})/$', 'archive_year', dict(info_dict, template_name='events/list.html')),
	(r'^$', 'archive_index', dict(info_dict, template_name='events/list.html'))
)