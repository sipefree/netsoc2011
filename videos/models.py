from django.db import models
from django.contrib.syndication.feeds import Feed
from django.contrib.sitemaps import Sitemap

from tagging.fields import TagField
from tagging.models import Tag
import settings

class Video(models.Model):
	title = models.CharField(max_length=200)
	slug = models.SlugField(
		help_text='Automatically built from the title.'
	)
	h264 = models.FileField(upload_to="videos/%Y/%m/%d", blank=True)
	webm = models.FileField(upload_to="videos/%Y/%m/%d", blank=True)
	theora = models.FileField(upload_to="videos/%Y/%m/%d", blank=True)
	
	class Meta:
		verbose_name_plural = 'videos'
	
	def __unicode__(self):
		return u'%s' % self.title
		
