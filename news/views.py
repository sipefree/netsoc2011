from django.http import HttpResponse,Http404
from pages.models import Page
from django.template import Context, loader
from django.shortcuts import render_to_response
from netsoc2011.news import models
from django.core.exceptions import ObjectDoesNotExist
import datetime
import time
import netsoc2011

def news_archive_index(request):
	qs = models.Entry.objects.filter(status=1)
	date_list = qs.dates('pub_date', 'year')[::-1]
	if not date_list:
		context = {'app': "Netsoc Latest News"}
		return render_to_response('nothinghere.html', context)
	else:
		latest = qs.order_by('-pub_date')
	
	context = {
		'date_list': date_list,
		'latest': latest,
		'request': request,
		'latest_news': netsoc2011.news.models.Entry.objects.latest()
	}
	return render_to_response('news/list.html', context)

def news_search(request):
	qs = models.Entry.objects.filter(body_html__icontains=request.GET.get('query', ''))
	context = {
		'latest': qs,
		'request': request,
		'latest_news': netsoc2011.news.models.Entry.objects.latest(),
		'query': request.GET.get('query', '')
	}
	return render_to_response('news/search.html', context)


def news_archive_year(request):
	pass

def news_detail(request, year, month, day, slug):
	qs = models.Entry.objects.filter(status=1)
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
	
	context = {'object': obj, 'latest_news': netsoc2011.news.models.Entry.objects.latest()}
	
	return render_to_response('news/detail.html', context)