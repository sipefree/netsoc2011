from django.db import models
from django.contrib.sitemaps import Sitemap

class Page(models.Model):
	title = models.CharField(max_length=200)
	slug = models.SlugField()
	body_html = models.TextField(blank=True)
	PUB_STATUS = (
		(0, 'Do not show in bar'),
		(1, 'Show in bar'),
	)
	status = models.IntegerField(choices=PUB_STATUS)
	SHOW_IN_BAR = (
		(0, 'Do not show'),
		(1, 'Show')
	)
	
	def __unicode__(self):
		return u'%s'%(self.title)
	
	def get_absolute_url(self):
		return "/pages/%s/" % (self.slug)