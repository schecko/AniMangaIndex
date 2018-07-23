from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django import forms
from django.db import connection
# from django.core.validators import MaxValueValidator, MinValueValidator

from .models import *
from .buildDB import *

import logging

logger = logging.getLogger(__name__)

LOGIN_KEY = 'userID'

class LoginForm(forms.Form):
	userID = forms.CharField(label = 'UserName', max_length = 255)
	password = forms.CharField(label = "Password", max_length = 255)

class RatingForm(forms.Form):
	newRating = forms.IntegerField(label = 'Please enter new rating between 0 and 10')
	
def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]

def dictfetchone(cursor):
	try:
		return dictfetchall(cursor)[0]
	except IndexError:
		return None
    #columns = [col[0] for col in cursor.description]
    #return dict(zip(columns, [cursor.fetchone()]))


def login(request):
	if request.method == 'POST':
		form = LoginForm(request.POST)

		if form.is_valid():
			with connection.cursor() as cursor:
				cursor.execute("select * from main_user where userID = %s", [form.data[LOGIN_KEY]])
				user = dictfetchone(cursor)

			if user:
				logger.critical("user exists")
				# user does exist, check their password
				b = form.data['password']
				a = user['password']
				if form.data['password'] == user['password']:
					logger.critical("user password is valid")
					request.session[LOGIN_KEY] = form.data[LOGIN_KEY]
					return HttpResponseRedirect('..')
				else:
					form.add_error('password', 'invalid password')
					return render(	request, 
									'main/login.html',
									{ 'form': form })
			else:
				logger.critical("user does not exist")
				# user does not exist, create them silently
				with connection.cursor() as cursor:
					cursor.execute("insert into main_user(userID, privileges, password) values ( %s, 0, %s )", [form.data[LOGIN_KEY], form.data['password']])

				# check that the new user was created, then send them back to the index.
				if User.objects.get(pk = form.data[LOGIN_KEY]):
					logger.critical("success in creating a new user")
					request.session[LOGIN_KEY] = form.data[LOGIN_KEY]
					logger.critical(form.data[LOGIN_KEY])
					logger.critical(request.session[LOGIN_KEY])
					return HttpResponseRedirect('..')
				else:
					form.add_error(LOGIN_KEY, 'internal error, try again')
					return render(	request, 
									'main/login.html',
									{ 'form': form })
	else:
		form = LoginForm()

		return render(	request, 
						'main/login.html',
						{ 'form': form })

def logout(request):
	try:
		del request.session[LOGIN_KEY]
	except:
		pass
	return HttpResponseRedirect('..')

def changeRating(request, contentID):
	if request.method == 'POST':
		form = RatingForm(request.POST)
		newRating = int(request.POST.get('newRating'))
		if form.is_valid():
			if (newRating <= 11 and newRating >= 0):
				cursor = connection.cursor()
				cursor.execute("UPDATE main_content SET rating = %s WHERE contentID = %s" % (newRating, contentID))
				result = cursor.fetchall()

				return HttpResponseRedirect('..')
			
			else:
				form.add_error('newRating', 'invalid rating')
				return render(request, 'content/changeRating.html', { 'form': form })
	else:
		form = RatingForm()
		return render(request, 'content/changeRating.html', { 'form': form })

def index(request):
	try:
		uid = request.session.get('userID')
		user = User.objects.get(pk = uid)
	except:
		user = None
	
	dbStatus = Content.objects.all()
	if not dbStatus:
		fillDB()
	
	contentData = 0
	creatorData = 0
		
	viewall = str(request.GET.get('viewall'))
	if viewall == "Content":
		contentData = Content.objects.raw('SELECT * FROM main_content')
		
		# Checking the query result, set to 0 if nothing returned
		try:
			contentData[0].contentID
		except IndexError:
			contentData = 0
	elif viewall == "Creator":
		creatorData = Creator.objects.raw('SELECT * FROM main_creator')
		
		# Checking the query result, set to 0 if nothing returned
		try:
			creatorData[0].creatorID
		except IndexError:
			creatorData = 0

	operand = str(request.GET.get('operand'))
	year = str(request.GET.get('year'))
	if operand == "Bigger":
		contentData = Content.objects.raw('SELECT * FROM main_content WHERE %s > date' % year)
		
		# Checking the query result, set to 0 if nothing returned
		try:
			contentData[0].contentID
		except IndexError:
			contentData = 0
	elif operand == "Same":
		contentData = Content.objects.raw('SELECT * FROM main_content WHERE %s = date' % year)
		
		# Checking the query result, set to 0 if nothing returned
		try:
			contentData[0].contentID
		except IndexError:
			contentData = 0
	elif operand == "Smaller":
		contentData = Content.objects.raw('SELECT * FROM main_content WHERE %s < date' % year)
		
		# Checking the query result, set to 0 if nothing returned
		try:
			contentData[0].contentID
		except IndexError:
			contentData = 0
	
	try:
		logger.critical("key is %s " % request.session[LOGIN_KEY])
		loggedIn = True
	except:
		logger.critical("key is nothing ")
		loggedIn = False

	template = loader.get_template('main/index.html')
	context = {
		'contentList': contentData,
		'creatorList': creatorData,
		'loggedIn': loggedIn
	}
	return HttpResponse(template.render(context, request))

def contentDetail(request, contentID):	
	template = loader.get_template('content/content.html')
	
	#Check to see if the tables are filled before proceeding to query
	contentList = Content.objects.all()
	creatorList = Creator.objects.all()
	createList = Create.objects.all()
	if not (contentList or creatorList or createList):
		return HttpResponse("No content available")
		
	# Queries
	contentData = Content.objects.raw('SELECT * FROM main_content WHERE contentID = %s' % contentID)	
	creatorData = Creator.objects.raw('SELECT * FROM main_create A, main_creator B WHERE A.creator_id = B.creatorID AND A.content_id = %s' % contentID)
	sourceData = Content.objects.raw('SELECT A.contentID, B.contentID, B.type FROM main_content A, main_content B WHERE A.source_id = B.contentID AND A.contentID = %s' % contentID) 
	
	# Checking the query result, set to 0 if nothing returned
	try:
		contentData[0].contentID
	except IndexError:
		contentData = 0
	
	try:
		creatorData[0].creatorID
	except IndexError:
		creatorData = 0
	
	try:
		sourceData[0].type
	except IndexError:
		sourceData = 0
		
	context = {
		'contentList': contentData,
		'sourcetype': sourceData,
		'creatorList': creatorData
		
	}
	return HttpResponse(template.render(context, request))

def creatorDetail(request, creatorID):	
	template = loader.get_template('creator/creator.html')
	
	#Check to see if the tables are filled before proceeding to query
	contentList = Content.objects.all()
	creatorList = Creator.objects.all()
	createList = Create.objects.all()
	if not (contentList or creatorList or createList):
		return HttpResponse("No content available")
	
	# Queries
	creatorData = Creator.objects.raw('SELECT creatorID, name, gender, birthday FROM main_creator WHERE creatorID = %s' % creatorID)
	contentData = Content.objects.raw('SELECT * FROM main_create A, main_content B WHERE A.content_id = B.contentID AND A.creator_id = %s' % creatorID)

	# Checking the query result, set to 0 if nothing returned
	try:
		creatorData[0].creatorID
	except IndexError:
		creatorData = 0
		
	try:
		contentData[0].contentID
	except IndexError:
		contentData = 0
		
	context = {
		'creatorList': creatorData,
		'contentList': contentData
	}
	return HttpResponse(template.render(context, request))
	
def genreDetail(request):	
	genre = str(request.GET.get('genre'))
	template = loader.get_template('genre/genre.html')
	#Check to see if the tables are filled before proceeding to query
	contentList = Content.objects.all()
	if not (contentList):
		return HttpResponse("No content available")

	# Queries
	contentData = Content.objects.raw('SELECT * FROM main_content WHERE genre LIKE "%s"' % (genre))

	# Checking the query result, set to 0 if nothing returned		
	try:
		contentData[0].contentID
	except IndexError:
		contentData = 0
		
	context = {
		'contentGenre': genre,
		'contentList': contentData
	}
	return HttpResponse(template.render(context, request))