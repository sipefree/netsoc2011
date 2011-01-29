from django.db import models
from django.contrib.syndication.feeds import Feed
from django.contrib.sitemaps import Sitemap

from tagging.fields import TagField
from tagging.models import Tag

class Entry(models.Model):
	title = models.CharField(max_length=200)
	slug = models.SlugField(
		unique_for_date='pub_date',
		help_text='Automatically built from the title.'
	)
	body_html = models.TextField(blank=True)
	pub_date = models.DateTimeField('Date published')
	tags = TagField()
	enable_comments = models.BooleanField(default=True)
	PUB_STATUS = (
		(0, 'Draft'),
		(1, 'Published')
	)
	status = models.IntegerField(choices=PUB_STATUS)
	
	class Meta:
		ordering = ('-pub_date',)
		get_latest_by = 'pub_date'
		verbose_name_plural = 'entries'
	
	def __unicode__(self):
		return u'%s' % self.title
	
	def get_absolute_url(self):
		return "/news/%s/%s/" % (self.pub_date.strftime("%Y/%m/%d").lower(), self.slug)
	
	def get_previous_published(self):
		return self.get_previous_by_pub_date(status__exact=1)
	
	def get_next_published(self):
		return self.get_next_by_pub_date(status__exact=1)
	
	def get_tags(self):
		return Tag.objects.get_for_object(self)
		
