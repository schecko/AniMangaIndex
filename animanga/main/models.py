from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from enum import Enum

class User(models.Model):
	userID = models.CharField(max_length = 255, primary_key = True)
	privileges = models.BooleanField()
	password = models.CharField(max_length = 255)

class Studio(models.Model):
	name = models.CharField(primary_key = True, max_length = 255)
	founded = models.IntegerField()

class Content(models.Model):
	contentID = models.IntegerField(primary_key = True)
	
	class ContentType(Enum):
		Manga = 0
		Book = 1
		Anime = 2

	type = models.IntegerField(choices = [ (tag.value, tag.name) for tag in ContentType ])
	title = models.CharField(max_length = 255)
	complete = models.BooleanField()
	rating = models.IntegerField(validators = [MaxValueValidator(5), MinValueValidator(0)])
	date = models.IntegerField()

	class Genre(Enum):
		Mystery = 0
		Drama = 1
		SciFi = 2
		Action = 3
		Fantasy = 4
		Comedy = 5
		Mecha = 6

	genre = models.IntegerField(choices = [ (tag.value, tag.name) for tag in Genre ])
	source = models.ForeignKey(  'self', 
								unique = False,
								blank = True,
								null = True,
								on_delete = models.SET_NULL)

class FavoriteContent(models.Model):
	userID = models.ForeignKey( User, 
								unique = False, 
								on_delete = models.CASCADE)

	contentID = models.ForeignKey(  Content, 
									unique = False,
									on_delete = models.CASCADE)

	class Meta:
		unique_together = (( "userID", "contentID"), )

class Creator(models.Model):
	creatorID = models.IntegerField(primary_key = True)
	birthday = models.IntegerField()
	gender = models.CharField(max_length = 255)
	name = models.CharField(max_length = 255)

class License(models.Model):
	contentID = models.ForeignKey(  Content,
									unique = False,
									on_delete = models.CASCADE)
	studio = models.ForeignKey( Studio,
								unique = False,
								on_delete = models.CASCADE)
	publisher = models.CharField(max_length = 255)

	class Meta:
		unique_together = (( "contentID", "studio"), )

class Hire(models.Model):
	studio = models.ForeignKey( Studio, 
								unique = False,
								on_delete = models.DO_NOTHING)
	creator = models.ForeignKey(Creator,
								unique = False,
								on_delete = models.DO_NOTHING)

	class Meta:
		unique_together = (( "studio", "creator"), )

class Create(models.Model):
	content = models.ForeignKey(Content,
								unique = False,
								on_delete = models.CASCADE)
	creator = models.ForeignKey(Creator,
								unique = False,
								on_delete = models.CASCADE)

	class Meta:
		unique_together = (( "content", "creator"), )
	
	class Role(Enum):
		Artist = 0
		Director = 1
		Animator = 2
		Author = 3

	role = models.IntegerField(choices = [ (tag.value, tag.name) for tag in Role ])

class VolumeSeason(models.Model):
	contentID = models.ForeignKey(  Content, 
									on_delete = models.CASCADE,
									unique = False)
	num = models.IntegerField()
	title = models.CharField(max_length = 225)

	class Meta:
		unique_together = (( "contentID", "num"), )
