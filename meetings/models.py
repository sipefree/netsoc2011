from django.db import models
from django.contrib.syndication.feeds import Feed
from django.contrib.sitemaps import Sitemap

from tagging.fields import TagField
from tagging.models import Tag
import settings

class MeetingInfo(models.Model):
	location = models.CharField(max_length=200)
	time = models.CharField(max_length=200)
	class Meta:
		verbose_name_plural = 'Meeting Info'

class Minutes(models.Model):
	body_html = models.TextField(blank=True)
	pub_date = models.DateTimeField('Date published')
	class Meta:
		ordering = ('-pub_date',)
		get_latest_by = 'pub_date'
		verbose_name_plural = 'Minutes'
	
	def __unicode__(self):
		return u'%s' % self.pub_date
	
	def get_absolute_url(self):
		return "/meetings/%s/" % self.id


