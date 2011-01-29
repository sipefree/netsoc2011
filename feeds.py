from django.contrib.syndication.views import Feed
from netsoc2011.news.models import Entry
from netsoc2011.events.models import Event

class LatestNewsFeed(Feed):
	title = "Netsoc Latest News"
	link = "/news/"
	description = "Latest updates and news from the Dublin University Internet Society."
	
	def items(self):
		return Entry.objects.order_by('-pub_date')[:10]
	
	def item_title(self, item):
		return item.title
	
	def item_description(self, item):
		return item.body_html

class LatestEventsFeed(Feed):
	title = "Netsoc Events"
	link = "/events/"
	description = "Events and happenings from the Dublin University Internet Society"
	
	def items(self):
		return Event.objects.order_by('-event_date')[:10]
	
	def item_title(self, item):
		return item.title
	
	def item_description(self, item):
		return "Location: %s<br />Date: %s<br /><br />%s" % (item.location, item.event_date, item.body_html)
