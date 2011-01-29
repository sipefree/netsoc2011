from django.contrib import admin

from netsoc2011.videos.models import Video

class VideoAdmin(admin.ModelAdmin):
	list_display = ('title', 'slug')
	search_fields = ['title', 'description']
	prepopulated_fields = {"slug": ('title',)}
	fieldsets = (
		(
			None,
			{
				'fields': (
					('title'),
					'h264',
					'webm',
					'theora',
					'slug',
				)
			}
		),
	)

admin.site.register(Video, VideoAdmin)
