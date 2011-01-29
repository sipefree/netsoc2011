from django.contrib import admin

from netsoc2011.pages.models import Page

class PageAdmin(admin.ModelAdmin):
	list_display = ('title', 'slug', 'status')
	search_fields = ['title', 'body_html']
	prepopulated_fields = {"slug": ('title',)}
	fieldsets = (
		(None, {'fields': (('title', 'status'), 'body_html', 'slug')}),
	)

admin.site.register(Page, PageAdmin)