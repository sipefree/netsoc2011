from django.contrib import admin
from netsoc2011.meetings.models import MeetingInfo
from netsoc2011.meetings.models import Minutes

class MinutesAdmin(admin.ModelAdmin):
	list_display = ('pub_date',)
	search_fields = ['body_html']
	fieldsets = (
		(
			None,
			{
				'fields': (
					'pub_date',
					'body_html',
				)
			}
		),
	)

class MeetingInfoAdmin(admin.ModelAdmin):
	list_display = ('location', 'time')
	fieldsets = (
		(
			None,
			{
				'fields': (
					'location',
					'time',
				)
			}
		),
	)

admin.site.register(Minutes, MinutesAdmin)
admin.site.register(MeetingInfo, MeetingInfoAdmin)