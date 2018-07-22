from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import *
from .buildDB import *

def index(request):
	contentList = Content.objects.all()
	if not contentList:
		fillDB()

	template = loader.get_template('main/index.html')
	context = {
		'contentList': contentList
	}
	return HttpResponse(template.render(context, request))

def contentDetail(request, contentID):	

	data = Content.objects.filter(contentID=contentID)
	return HttpResponse("Content info for %s (contentID = %s)" % (data[0].title, contentID))

def creatorDetail(request, creatorID):	
	template = loader.get_template('creator/creator.html')
	contentList = Content.objects.all()
	creatorList = Creator.objects.all()
	createList = Create.objects.all()
	if not (contentList or creatorList or createList):
		return HttpResponse("No content available")
		
	creatorData = Creator.objects.raw('SELECT creatorID, name, gender, birthday FROM main_creator WHERE creatorID = %s' % creatorID)
	contentData = Content.objects.raw('SELECT * FROM main_create A, main_content B WHERE A.content_id = B.contentID AND A.creator_id = %s' % creatorID)

	context = {
		'creatorName': creatorData[0].name,
		'creatorGender': "Female" if creatorData[0].gender else "Male",
		'creatorBday': creatorData[0].birthday,
		'contentList': contentData
	}
	return HttpResponse(template.render(context, request))