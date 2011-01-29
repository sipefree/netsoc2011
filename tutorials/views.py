from django.http import HttpResponse,Http404
from pages.models import Page
from django.template import Context, loader
from django.shortcuts import render_to_response
from netsoc2011.tutorials import models
from django.core.exceptions import ObjectDoesNotExist
import datetime
import time
import netsoc2011

def tutorial_archive_index(request):
	qs = models.Tutorial.objects
	date_list = qs.dates('pub_date', 'year')[::-1]
	if not date_list:
		context = {'app': "Netsoc Tutorials"}
		return render_to_response('nothinghere.html', context)
	else:
		latest = qs.order_by('-starred', '-pub_date')
	
	context = {
		'date_list': date_list,
		'tutorials': latest,
		'request': request,
		'latest_news': netsoc2011.news.models.Entry.objects.latest()
	}
	return render_to_response('tutorials/list.html', context)

def tutorials_search(request):
	qs = models.Tutorial.objects.filter(description__icontains=request.GET.get('query', ''))
	context = {
		'tutorials': qs,
		'request': request,
		'latest_news': netsoc2011.news.models.Entry.objects.latest(),
		'query': request.GET.get('query', '')
	}
	return render_to_response('tutorials/search.html', context)

def tutorial_detail(request, year, month, day, slug):
	qs = models.Tutorial.objects
	try:
		tt = time.strptime('%s-%s-%s' % (year, month, day), '%Y-%m-%d')
		date = datetime.date(*tt[:3])
	except ValueError:
		raise Http404
	
	now = datetime.datetime.now()
	lookup_kwargs = {
		'pub_date__range': (datetime.datetime.combine(date, datetime.time.min), datetime.datetime.combine(date, datetime.time.max)),
		'slug__exact': slug
	}
	try:
		obj = qs.get(**lookup_kwargs)
	except ObjectDoesNotExist:
		raise Http404
	
	context = {'tutorial': obj, 'latest_news': netsoc2011.news.models.Entry.objects.latest()}
	
	return render_to_response('tutorials/detail.html', context)