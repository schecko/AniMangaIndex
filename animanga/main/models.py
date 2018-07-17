from django.db import models
from django.core.validators import MaxValueIndicator, MinValueIndicator
from enum import Enum

class User(models.Model):
	userID = models.IntegerField(primary_key = True)
	privileges = models.BoolField()
	password = models.CharField(max_length = 255)
	email = models.CharField(max_length = 255)

class Studio(model.Model):
	name = models.CharField(primary_key = True, max_length = 255)
	founded = models.DateField()

class Content(models.Model):
	contentID = models.IntegerField(primary_key = True)
	
	class Type(Enum):
		Manga = 0
		Book = 1
		Anime = 2

	type = models.IntegerField(choices = [ (tag.value, tag) for tag in Type ])
	title = models.CharField(max_length = 200)
	complete = models.BoolField()
	rating = models.IntegerField(validators = [MaxValueIndicator(5), MinValueIndicator(0)])
	date = models.DateField()
	genre = models.CharField()

class FavoriteContent(models.Model):
	userID = models.ForeignKey( User, 
								primary_key = True, 
								on_delete = models.DO_NOTHING)

	contentID = models.ForeignKey(  Content, 
									primary_key = True,
									on_delete = models.DO_NOTHING)

class Creator(model.Model):
	creatorID = models.IntegerField(primary_key = True)
	birthday = models.DateField()
	genre = models.BoolField()
	name = models.CharField(max_length = 255)

class Studio(model.Model):
	name = models.CharField(max_length = 255,
							primary_key = True,
							on_delete = models.DO_NOTHING)
	founded = models.DateField()

class Licenses(models.Model):
	contentID = models.ForeignKey(  Content,
									primary_key = True,
									on_delete = models.CASCADE)
	studio = models.ForeignKey( Studio,
								primary_key = True,
								on_delete = models.DO_NOTHING)
	publisher = models.CharField(max_length = 255)

class Hires(models.Model):
	studio = models.ForeignKey( Studio, 
								primary_key = True,
								on_delete = models.DO_NOTHING)
	creator = models.ForeignKey(Creator,
								primary_key = True,
								on_delete = models.DO_NOTHING)

class Creates(models.Model):
	content = models.ForeignKey(Content,
								primary_key = True,
								on_delete = models.CASCADE)
	creator = models.ForeignKey(Creator,
								primary_key = True,
								on_delete = models.DO_NOTHING)
	
	class Role(Enum):
		Artist = 0
		Director = 1
		Animator = 2
		Author = 3

	role = models.IntegerField(choice = [ (tag.value, tag) for tag in Role ])

class VolumeSeason(model.Model):
	ContentID = models.ForeignKey(  Content, 
									on_delete = models.CASCADE, 
									primary_key = True)
	num = models.IntegerField()
	