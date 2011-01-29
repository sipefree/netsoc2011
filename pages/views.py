from django.http import HttpResponse,Http404
from pages.models import Page
from django.template import Context, loader
from django.shortcuts import render_to_response
import netsoc2011

def site_index(request):
	context = {
		'latest_news': netsoc2011.news.models.Entry.objects.latest()
	}
	return render_to_response('index.html', context)

def detail(request, slug):
	try:
		page = Page.objects.get(slug=slug)
	except Page.DoesNotExist:
		raise Http404
	
	context = {
		'page': page,
		'latest_news': netsoc2011.news.models.Entry.objects.latest(),
		'pages': Page.objects.filter(status=1)
	}
		
	return render_to_response('pages/detail.html', context)