from django.shortcuts import render
from django.http import HttpResponse
from main.models import Content

def index(request):
    return HttpResponse("Hello World. You're at the manga index")

def contentDetail(request, contentID):
	data = Content.objects.filter(contentID=contentID)
	return HttpResponse("Content info for %s (contentID = %s)" % (data[0].title, contentID))

def creatorDetail(request, creatorID):
	return HttpResponse("Hello creator detailed world %s" % creatorID)