from django.http import HttpResponse,Http404
from pages.models import Page
from django.template import Context, loader
from django.shortcuts import render_to_response
from netsoc2011.meetings import models
from django.core.exceptions import ObjectDoesNotExist
import datetime
import time
import netsoc2011

def meetings_archive_index(request):
	qs = models.Minutes.objects
	latest = qs.order_by('-pub_date')
	context = {
		'minutes': latest,
		'request': request,
		'meetinginfo': models.MeetingInfo.objects.all()[0],
		'latest_news': netsoc2011.news.models.Entry.objects.latest()
	}
	return render_to_response('meetings/list.html', context)

def meetings_search(request):
	qs = models.Minutes.objects.filter(body_html__icontains=request.GET.get('query', ''))
	context = {
		'minutes': qs,
		'request': request,
		'latest_news': netsoc2011.news.models.Entry.objects.latest(),
		'query': request.GET.get('query', '')
	}
	return render_to_response('meetings/search.html', context)

def meeting_detail(request, id):
	qs = models.Minutes.objects
	lookup_kwargs = {
		'id__exact': id
	}
	try:
		obj = qs.get(**lookup_kwargs)
	except ObjectDoesNotExist:
		raise Http404
	
	context = {
		'minutes': obj,
		'latest_news': netsoc2011.news.models.Entry.objects.latest(),
	}
	return render_to_response('meetings/detail.html', context)