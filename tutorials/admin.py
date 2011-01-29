from django.contrib import admin

from netsoc2011.tutorials.models import Tutorial

class TutorialAdmin(admin.ModelAdmin):
	list_display = ('title', 'slug', 'pub_date')
	search_fields = ['title', 'description']
	prepopulated_fields = {"slug": ('title',)}
	fieldsets = (
		(
			None,
			{
				'fields': (
					('title'),
					'starred',
					'description',
					('pub_date', 'enable_comments'),
					('slides', 'video'),
					'upload_to_scribd',
					'tags',
					'slug',
					('scribd_doc_id', 'scribd_doc_key'),
				)
			}
		),
	)

admin.site.register(Tutorial, TutorialAdmin)
