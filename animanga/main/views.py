from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from main.models import *
from main.buildDB import *

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
	contentList = Content.objects.all()
	if not contentList:
		fillDB()

	data = Content.objects.filter(contentID=contentID)
	return HttpResponse("Content info for %s (contentID = %s)" % (data[0].title, contentID))

def creatorDetail(request, creatorID):
	creatorList = Creator.objects.all()
	if not creatorList:
		fillDB()
	
	creatorData = Creator.objects.raw('SELECT creatorID, name, gender, birthday FROM main_creator WHERE creatorID = %s' % creatorID)
	contentList = Content.objects.raw('SELECT * FROM main_create A, main_content B WHERE A.content_id = B.contentID AND A.creator_id = %s' % creatorID)

	template = loader.get_template('creator/creator.html')
	context = {
		'creatorName': creatorData[0].name,
		'creatorGender': "Female" if creatorData[0].gender else "Male",
		'creatorBday': creatorData[0].birthday,
		'contentList': contentList
	}
	return HttpResponse(template.render(context, request))