from django.contrib import admin
from netsoc2011.events.models import Event

class EventAdmin(admin.ModelAdmin):
	list_display = ('title', 'event_date', 'location', 'speaker', 'enable_comments', 'event_type')
	search_fields = ['title', 'body_html', 'location', 'speaker']
	list_filter = ('event_date', 'enable_comments', 'event_type')
	prepopulated_fields = {"slug": ('title',)}
	fieldsets = (
		(None, {'fields': (('title', 'event_type'), 'location', 'speaker', 'body_html', ('event_date', 'enable_comments'), 'tags', 'facebook', 'slug')}),
	)

admin.site.register(Event, EventAdmin)