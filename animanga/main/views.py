from django.shortcuts import render
from django.http import HttpResponse
from main.models import *
from main.init import *

def index(request):
    return HttpResponse("Hello World. You're at the manga index")

def contentDetail(request, contentID):
	data = Content.objects.filter(contentID=contentID)
	return HttpResponse("Content info for %s (contentID = %s)" % (data[0].title, contentID))

def creatorDetail(request, creatorID):
	data = Creator.objects.filter(creatorID=creatorID)
	return HttpResponse("Creator info for %s (contentID = %s)" % (data[0].name, creatorID))