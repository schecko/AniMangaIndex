from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello World. You're at the manga index")

def contentDetail(request, contentID):
	return HttpResponse("Hello detailed world: %s" % contentID)

def creatorDetail(request, creatorID):
	return HttpResponse("Hello creator detailed world %s" % creatorID)