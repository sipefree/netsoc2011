from django.db import models
from django.contrib.syndication.feeds import Feed
from django.contrib.sitemaps import Sitemap

from tagging.fields import TagField
from tagging.models import Tag
import scribd
import settings

class Tutorial(models.Model):
	title = models.CharField(max_length=200)
	slug = models.SlugField(
		unique_for_date='pub_date',
		help_text='Automatically built from the title.'
	)
	starred = models.BooleanField()
	description = models.TextField(blank=True)
	upload_to_scribd = models.BooleanField()
	slides = models.FileField(upload_to="slides/%Y/%m/%d", blank=True)
	video = models.ForeignKey('videos.Video', blank=True, null=True)
	pub_date = models.DateTimeField('Date published')
	tags = TagField()
	enable_comments = models.BooleanField(default=True)
	scribd_doc_id = models.CharField(max_length=100, blank=True)
	scribd_doc_key = models.CharField(max_length=100, blank=True)
	
	class Meta:
		ordering = ('-pub_date',)
		get_latest_by = 'pub_date'
		verbose_name_plural = 'tutorials'
	
	def __unicode__(self):
		return u'%s' % self.title
	
	def get_absolute_url(self):
		return "/tutorials/%s/%s/" % (self.pub_date.strftime("%Y/%m/%d").lower(), self.slug)
	
	def get_tags(self):
		return Tag.objects.get_for_object(self)
	
	def save(self):
		super(Tutorial, self).save()
		scribd.config(settings.SCRIBD_API_KEY, settings.SCRIBD_API_SECRET)
		if self.slides and self.upload_to_scribd:
			self.upload_to_scribd = False
			try:
				print "Uploading %s to Scribd" % self.slides
				doc = scribd.api_user.upload(open(self.slides.path))
				self.scribd_doc_id = doc.id
				self.scribd_doc_key = doc.access_key
				doc.title = self.title
				doc.description = self.title
				doc.access = 'public'
				doc.language = 'en'
				doc.tags = 'netsoc'
				doc.show_ads = 'false'
				doc.save()
				super(Tutorial, self).save()
			except scribd.ResponseError, err:
				print 'Scribd failed: code=%d, error=%s' % (err.errno, err.strerror)
		
