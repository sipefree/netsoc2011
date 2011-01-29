from django.views.generic.list_detail import object_detail,object_list
from tagging.models import Tag,TaggedItem
from news.models import Entry

def tag_detail(request, slug):
	unslug = slug.replace('-', ' ')
	tag = Tag.objects.get(name=unslug)
	qs = TaggedItem.objects.get_by_model(Entry, tag)
	return object_detail(request, queryset=qs, slug=tag, template_name='tags/detail.html')