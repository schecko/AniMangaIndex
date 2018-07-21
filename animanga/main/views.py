from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import *

from .buildDB import fillDB

def index(request):
	contentList = Content.objects.all()

	#if not contentList:
	#	fillDB()

	template = loader.get_template('main/index.html')
	context = {
		'contentList': contentList
	}
	return HttpResponse(template.render(context, request))

def contentDetail(request, contentID):
	return HttpResponse("Hello detailed world: %s" % contentID)

def creatorDetail(request, creatorID):
	return HttpResponse("Hello creator detailed world %s" % creatorID)
