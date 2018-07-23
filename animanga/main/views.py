from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django import forms
from django.db import connection

from .models import *
from .buildDB import *

import logging

logger = logging.getLogger(__name__)

LOGIN_KEY = 'userID'

class LoginForm(forms.Form):
	userID = forms.CharField(label = 'UserName', max_length = 255)
	password = forms.CharField(label = "Password", max_length = 255)

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

def index(request):
	try:
		uid = request.session.get('userID')
		user = User.objects.get(pk = uid)
	except:
		user = None

	contentList = Content.objects.all()
	if not contentList:
		fillDB()

	try:
		logger.critical("key is %s " % request.session[LOGIN_KEY])
		loggedIn = True
	except:
		logger.critical("key is nothing ")
		loggedIn = False

	template = loader.get_template('main/index.html')
	context = {
		'contentList': contentList,
		'loggedIn': loggedIn,
		#'userName': user.userName,
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