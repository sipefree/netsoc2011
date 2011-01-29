from django.db import models
from django.contrib.syndication.feeds import Feed
from django.contrib.sitemaps import Sitemap

from tagging.fields import TagField
from tagging.models import Tag

class Event(models.Model):
	title = models.CharField(max_length=200)
	location = models.CharField(max_length=200, blank=True)
	speaker = models.CharField(max_length=200, blank=True)
	slug = models.SlugField(
		unique_for_date='event_date',
		help_text='Automatically built from the title.'
	)
	body_html = models.TextField(blank=True)
	event_date = models.DateTimeField('Date of event')
	tags = TagField()
	enable_comments = models.BooleanField(default=True)
	EVENT_TYPE = (
		(0, 'Tutorial'),
		(1, 'Talk'),
		(2, 'LAN Party'),
		(3, 'AGM'),
		(4, 'EGM'),
		(5, 'Event')
	)
	event_type = models.IntegerField(choices=EVENT_TYPE)
	facebook = models.URLField("URL of Facebook Event", blank=True)
	
	class Meta:
		ordering = ('-event_date',)
		get_latest_by = 'event_date'
		verbose_name_plural = 'Events'
	
	def __unicode__(self):
		return u'%s' % self.title
	
	def get_absolute_url(self):
		return "/events/%s/%s/" % (self.event_date.strftime("%Y/%m/%d").lower(), self.slug)
	
	def get_tags(self):
		return Tag.objects.get_for_object(self)
