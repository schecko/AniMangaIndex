from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django import forms
from django.db import connection

from .models import *
from .buildDB import *

import logging
from enum import Enum

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

def isLoggedIn(request):
	try:
		uid = request.session[LOGIN_KEY]
		return True, uid
	except:
		return False, None

def logout(request):
	try:
		del request.session[LOGIN_KEY]
	except:
		pass
	return HttpResponseRedirect('..')

class IndexQuery(Enum):
	Content = 0
	Creator = 1
	Joined = 2
	FavoriteContent = 3

def index(request):
	creatorData = None
	contentData = None
	joinedData = None
	loggedIn, userID = isLoggedIn(request)

	with connection.cursor() as cursor:
		cursor.execute('SELECT contentID, title, date, type, complete, rating, genre FROM main_content')
		contentData = dictfetchall(cursor)
		if not contentData:
			fillDB()
			cursor.execute('SELECT contentID, title, date, type, complete, rating, genre FROM main_content')
			contentData = dictfetchall(cursor)

		indexQuery = str(request.GET.get('indexQuery'))
		indexView = IndexQuery.Content.name # default
		if indexQuery == "Creator":
			cursor.execute('SELECT creatorID, name, gender, birthday FROM main_creator')
			creatorData = dictfetchall(cursor)
			indexView = IndexQuery.Creator.name
		elif indexQuery == "Joined":
			indexView = IndexQuery.Joined.name
			cursor.execute('select * from main_creator, main_content, main_create where content_id = contentID and creator_id = creatorID')
			joinedData = dictfetchall(cursor)
		elif indexQuery == "FavoriteContent":
			indexView = IndexQuery.FavoriteContent.name
			if loggedIn == True:
				cursor.execute("""
					select title, complete, rating, date, genre from 
					main_content, main_favoriteContent, main_user 
					where contentID_id = contentID and userID = userID_id and userID = %s
				""", [ userID ])
				contentData = dictfetchall(cursor)
			else:
				contentData = None

		template = loader.get_template('main/index.html')
		context = {
			'contentList': contentData,
			'creatorList': creatorData,
			'joinedList': joinedData,
			'loggedIn': loggedIn,
			'indexView': indexView,
		}
		return HttpResponse(template.render(context, request))

def isAdmin(request):
	try:
		with connection.cursor() as cursor:
			cursor.execute("select * from main_user where userID = %s", [ request.session[LOGIN_KEY] ])
			user = dictfetchone(cursor)

			if user['privileges'] == True:
				return True
			else:
				return False
	except:
		return False

def addFavorite(request, contentID):
	try:
		with connection.cursor() as cursor:
			cursor.execute("""
				select * 
				from main_user 
				where userID = %s""",
				[ request.session[LOGIN_KEY] ]
			)
			user = dictfetchone(cursor)

			cursor.execute("""
				insert into main_favoritecontent(userID_id, contentID_id)
				values (%s, %s)""", 
				[ user[LOGIN_KEY], contentID ]
			)
			return HttpResponseRedirect('/')
	except KeyError:
		# user is not logged in, direct to login
		return HttpResponseRedirect('/login')
	except: 
		return HttpResponseRedirect('/')

def nextFavorites(request):
	try:
		with connection.cursor() as cursor:
			# based on favorite content select similar (by genre) content  
			cursor.execute("""
				select contentID, title, complete, rating, date
				from main_content 
				where genre in 
				(
					 select genre 
					 from main_user, main_favoriteContent, main_content 
					 where userID_id = userID and contentID_id = contentID and userID = %s
				) except
				select contentID, title, complete, rating, date
				from main_content, main_favoriteContent, main_user
				where userID_id = userID and contentID_id = contentID and userID = %s
				""",
				[ request.session[LOGIN_KEY], request.session[LOGIN_KEY] ]
			)
			contentList = dictfetchall(cursor)

			return render(	request, 
					'main/nextFavorites.html',
					{ 'contentList': contentList })

	except KeyError:
		# user is not logged in, direct to login
		return HttpResponseRedirect('/login')		


def deleteContent(request, contentID):
	try:
		# user is logged in, check if they are admin
		with connection.cursor() as cursor:
			cursor.execute("select * from main_user where userID = %s", [ request.session[LOGIN_KEY] ])
			user = dictfetchone(cursor)

			if user['privileges'] == True:
				# user has credentials
				## NOTE: attempted both cursor and raw, both failed to work. 
				# the cursor seems to trigger some key constraint conditions that 
				# django performs in two steps, which does not happen with cursor as
				# the cursor is not properly checked by django. Using the model.raw method
				# seems to just be a no-op for who knows why. Performing the deletes in 
				# the admin page do work, and performing the deletes directly onto the sql 
				# do work as well using an external sql GUI, so this is certainly some django 
				# specific nonsense.
				# - raw method: (for marking)
				# cursor.execute("delete from main_content where contentID = %s", [contentID])
				# dictfetchone(cursor)
				# - model raw method: (for sanity)
				# Content.objects.raw("delete from main_content where contentID = %s" % contentID)
				# - working alternative using django's api:
				Content.objects.filter(contentID=contentID).delete()
				return HttpResponseRedirect('/')
			else:
				# user does not have credentials, just return to the previous page
				return HttpResponseRedirect('..')
	except KeyError:
		# user is not logged in, direct to login
		return HttpResponseRedirect('/login')

def contentDetail(request, contentID):
	cursor = connection.cursor()
	template = loader.get_template('content/content.html')

	newRating = request.GET.get('rating')
	if newRating != None:
		cursor.execute('UPDATE main_content SET rating = %s WHERE contentID = %s' % (newRating, contentID))

	# Queries
	cursor.execute('SELECT * FROM main_content WHERE contentID = %s' % contentID)
	contentData = dictfetchone(cursor)

	cursor.execute('SELECT * FROM main_create A, main_creator B WHERE A.creator_id = B.creatorID AND A.content_id = %s' % contentID)
	creatorData = dictfetchall(cursor)

	cursor.execute('SELECT count(*) number FROM main_create A, main_creator B WHERE A.creator_id = B.creatorID AND A.content_id = %s' % contentID)
	countCreatorData = dictfetchall(cursor)

	if contentData:
		cursor.execute('SELECT * from main_content where contentID = %s', [contentData['source_id']]) 
		sourceData = dictfetchone(cursor)

	cursor.execute('SELECT * FROM main_volumeseason where contentID_id = %s' % contentID)
	volumeseasons = dictfetchall(cursor)

	isSeason = False
	if contentData['type'] == Content.ContentType.Anime.name:
		isSeason = True

	admin = isAdmin(request)

	context = {
		'content': contentData,
		'source': sourceData,
		'creatorList': creatorData,
		'countCreator': countCreatorData,
		'volumeseasons': volumeseasons,
		'isSeason': isSeason,
		'isAdmin': admin,
		'loggedIn': isLoggedIn(request)
	}
	return HttpResponse(template.render(context, request))

def creatorDetail(request, creatorID):
	cursor = connection.cursor()	
	template = loader.get_template('creator/creator.html')

	# Queries
	cursor.execute('SELECT creatorID, name, gender, birthday FROM main_creator WHERE creatorID = %s' % creatorID)
	creatorData = dictfetchall(cursor)

	cursor.execute('SELECT * FROM main_create A, main_content B WHERE A.content_id = B.contentID AND A.creator_id = %s' % creatorID)
	contentData = dictfetchall(cursor)

	cursor.execute('SELECT count(*) number FROM main_create A, main_content B WHERE A.content_id = B.contentID AND A.creator_id = %s' % creatorID)
	countContentData = dictfetchall(cursor)

	context = {
		'creatorList': creatorData,
		'contentList': contentData,
		'countContent': countContentData
	}
	return HttpResponse(template.render(context, request))

def genreDetail(request):
	cursor = connection.cursor()
	genre = str(request.GET.get('genre'))
	template = loader.get_template('genre/genre.html')

	# Queries
	cursor.execute('SELECT * FROM main_content WHERE genre LIKE "%s"' % (genre))
	contentData = dictfetchall(cursor)

	cursor.execute('SELECT count(*) temp FROM main_content WHERE genre LIKE "%s"' % (genre))
	countContentData = dictfetchall(cursor)

	context = {
		'contentGenre': genre,
		'contentList': contentData,
		'countContent': countContentData
	}
	return HttpResponse(template.render(context, request))

def projectionDetail(request):
	contentData = None
	creatorData = None
	count = None
	cursor = connection.cursor()
	template = loader.get_template('main/projection.html')

	viewall = str(request.GET.get('viewall'))
	if viewall == "Content":
		cursor.execute('SELECT contentID, title, date, type, complete, rating FROM main_content')
		contentData = dictfetchall(cursor)

		cursor.execute('SELECT count(*) number FROM main_content')
		count = dictfetchall(cursor)

	elif viewall == "Creator":
		cursor.execute('SELECT creatorID, name, count(*) numberofworks FROM main_creator A, main_create B WHERE B.creator_id = A.creatorID GROUP BY creatorID')
		creatorData = dictfetchall(cursor)

		cursor.execute('SELECT count(*) number FROM main_creator')
		count = dictfetchall(cursor)

	context = {
		'contentList': contentData,
		'creatorList': creatorData,
		'count': count
	}
	return HttpResponse(template.render(context, request))

def selectionDetail(request):
	contentData = None
	count = None
	cursor = connection.cursor()
	template = loader.get_template('main/selection.html')

	operand = str(request.GET.get('operand'))
	year = request.GET.get('year')
	if operand == "before":
		cursor.execute('SELECT * FROM main_content WHERE %s > date' % year)
		contentData = dictfetchall(cursor)

		cursor.execute('SELECT count(*) number FROM main_content WHERE %s > date' % year)
		count = dictfetchall(cursor)

	elif operand == "on":
		cursor.execute('SELECT * FROM main_content WHERE %s = date' % year)
		contentData = dictfetchall(cursor)

		cursor.execute('SELECT count(*) number FROM main_content WHERE %s = date' % year)
		count = dictfetchall(cursor)

	elif operand == "after":
		cursor.execute('SELECT * FROM main_content WHERE %s < date' % year)	
		contentData = dictfetchall(cursor)

		cursor.execute('SELECT count(*) number FROM main_content WHERE %s < date' % year)
		count = dictfetchall(cursor)

	context = {
		'contentList': contentData,
		'displayingOperand': operand,
		'displayingYear': year,
		'count': count
	}
	return HttpResponse(template.render(context, request))

def nestedDetail(request):
    nestedData = None
    cursor = connection.cursor()
    template = loader.get_template('nested/nested.html')

 
   #Queries
    cursor.execute('SELECT contentID, content_id, creator_id, title, rating, COUNT(*) as avgcount FROM main_content, main_create WHERE content_id=contentID AND rating > (SELECT AVG(rating) from main_content GROUP BY genre) GROUP BY contentID')
    nestedData = dictfetchall(cursor)
    
    context = {
            'createList': nestedData
        }
    return HttpResponse(template.render(context, request))

def createDetail(request):
    createData = None
    cursor = connection.cursor()
    template = loader.get_template('create/create.html')

    #Queries
    cursor.execute('SELECT creatorID, name, count(*) count FROM main_creator, main_create WHERE creator_id = creatorID GROUP BY creatorID')
    createData = dictfetchall(cursor)

    context = {
        'createList': createData,
    }    
    return HttpResponse(template.render(context, request))

def divisionDetail(request):
    allCreatorStudioData = None
    cursor = connection.cursor()
    template = loader.get_template('division/division.html')

    #Queries
    cursor.execute('SELECT C.name, C.creatorID FROM main_creator C WHERE NOT EXISTS (SELECT * FROM main_studio L WHERE NOT EXISTS (SELECT H.creator_id FROM main_hire H WHERE L.name = H.studio_id AND C.creatorID = H.creator_id))')
    allCreatorStudioData = dictfetchall(cursor)

    context = {
        'allCreatorStudioList': allCreatorStudioData
    }    
    return HttpResponse(template.render(context, request))
