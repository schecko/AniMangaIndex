from django.db import connection
from .models import *

def fillDB():
	cursor = connection.cursor()

	# CREATE TABLE main_user(
	  # userID     VARCHAR(255) PRIMARY KEY,
	  # privileges INT,
	  # password   VARCHAR(255),
	# );
	# Inserting data into User table
	userInsert = [
		'INSERT INTO main_user(userID,privileges,password) VALUES ("eton",  1, 123)',
		'INSERT INTO main_user(userID,privileges,password) VALUES ("colin", 1, 123)',
		'INSERT INTO main_user(userID,privileges,password) VALUES ("linda", 1, 123)',
		'INSERT INTO main_user(userID,privileges,password) VALUES ("scott", 1, 123)',
		'INSERT INTO main_user(userID,privileges,password) VALUES ("test",  0, 123)',
	]

	i = 0
	for contents in userInsert:
		cursor.execute(str(userInsert[i]))
		i+=1
		result = cursor.fetchall()

	# CREATE TABLE main_studio(
	  # name    VARCHAR(255) PRIMARY KEY,variable
	  # founded DATE
	# );
	# Inserting data into Studio table	
	studioInsert = [
		'INSERT INTO main_studio(name,founded) VALUES ("White Fox",		"2007")',
		'INSERT INTO main_studio(name,founded) VALUES ("Studio Pierrot","1979")',
		'INSERT INTO main_studio(name,founded) VALUES ("Studio 3Hz",	"2013")',
		'INSERT INTO main_studio(name,founded) VALUES ("Ufotable",		"1997")',
		'INSERT INTO main_studio(name,founded) VALUES ("Studio Ghibli",	"1985")',
		'INSERT INTO main_studio(name,founded) VALUES ("Sunrise Studio","1972")',
		'INSERT INTO main_studio(name,founded) VALUES ("Gainax",		"1984")',
	]

	i = 0
	for contents in studioInsert:
		cursor.execute(str(studioInsert[i]))
		i+=1
		result = cursor.fetchall()

	# CREATE TABLE main_content(
	  # contentID INT PRIMARY KEY,
	  # type      VARCHAR(255),
	  # title     VARCHAR(255),
	  # complete  INT,
	  # rating    INT,
	  # date      DATE,
	  # genre     VARCHAR(255),
	  # source    INT,
	  # FOREIGN KEY (source) REFERENCES main_content(contentID) ON DELETE NO ACTION
	# );
	# Inserting data into Content table
	# Note: foreign keys in django automatically get appended with _id after the variable name
	contentInsert = [
		'INSERT INTO main_content(contentID,type,title,complete,rating,date,genre,source_id) VALUES (0,"Anime","Steins;Gate",1,9,"2018","Mystery",NULL)',
		'INSERT INTO main_content(contentID,type,title,complete,rating,date,genre,source_id) VALUES (1,"Anime","Tokyo Ghoul",1,7,"2018","Action",NULL)',
		'INSERT INTO main_content(contentID,type,title,complete,rating,date,genre,source_id) VALUES (2,"Anime","Sword Art Online",0,7,"2018","Fantasy",NULL)',
		'INSERT INTO main_content(contentID,type,title,complete,rating,date,genre,source_id) VALUES (3,"Book","Fate/Zero The Novel",1,7,"2006","Action",NULL)',
		'INSERT INTO main_content(contentID,type,title,complete,rating,date,genre,source_id) VALUES (4,"Manga","Fate/Zero",1,8,"2010","Action",3)',
		'INSERT INTO main_content(contentID,type,title,complete,rating,date,genre,source_id) VALUES (5,"Anime","Fate/Zero The Animation",1,9,"2011","Action",4)',
		'INSERT INTO main_content(contentID,type,title,complete,rating,date,genre,source_id) VALUES (6,"Anime","Spirited Away",2,10,"2001","Fantasy",NULL)',
		'INSERT INTO main_content(contentID,type,title,complete,rating,date,genre,source_id) VALUES (7,"Anime","Code Geass",2,10,"2006","Mecha",NULL)',
		'INSERT INTO main_content(contentID,type,title,complete,rating,date,genre,source_id) VALUES (8,"Manga","Gurren Lagann (Manga)",0,10,"2007","Mecha",NULL)',
		'INSERT INTO main_content(contentID,type,title,complete,rating,date,genre,source_id) VALUES (9,"Book","Gurren Lagann (Novel)",1,10,"2007","Mecha",NULL)',
		'INSERT INTO main_content(contentID,type,title,complete,rating,date,genre,source_id) VALUES (10,"Anime","Gurren Lagann (Anime)",2,10,"2007","Mecha",NULL)',
		'INSERT INTO main_content(contentID,type,title,complete,rating,date,genre,source_id) VALUES (11,"Anime","Bleach",2,6,"2004","Action",NULL)',
	]

	i = 0
	for contents in contentInsert:
		cursor.execute(str(contentInsert[i]))
		i+=1
		result = cursor.fetchall()

	# CREATE TABLE main_creator(
	  # creatorID INT PRIMARY KEY,
	  # birthday  DATE,
	  # gender    INT,
	  # name      VARCHAR(255)
	# );
	# Inserting data into Creator table	
	creatorInsert = [
		'INSERT INTO main_creator(creatorID,birthday,gender,name) VALUES (0,"1971","male","Kenichi Kawamura")',
		'INSERT INTO main_creator(creatorID,birthday,gender,name) VALUES (1,"1969","male","Jukki Hanada")',
		'INSERT INTO main_creator(creatorID,birthday,gender,name) VALUES (2,"1970","male","Chiyomaru Shikura")',
		'INSERT INTO main_creator(creatorID,birthday,gender,name) VALUES (3,"1985","male","Sui Ishida")',
		'INSERT INTO main_creator(creatorID,birthday,gender,name) VALUES (4,"1978","male","Shuhei Morita")',
		'INSERT INTO main_creator(creatorID,birthday,gender,name) VALUES (5,"1980","male","Chuji Mikasano")',
		'INSERT INTO main_creator(creatorID,birthday,gender,name) VALUES (6,"1974","male","Masayuki Sakoi")',
		'INSERT INTO main_creator(creatorID,birthday,gender,name) VALUES (7,"1972","male","Keiichi Sigsawa")',
		'INSERT INTO main_creator(creatorID,birthday,gender,name) VALUES (8,"1968","male","Yosuke Kuroda")',
		'INSERT INTO main_creator(creatorID,birthday,gender,name) VALUES (9,"1972","male","Gen Urobuchi")',
		'INSERT INTO main_creator(creatorID,birthday,gender,name) VALUES (10,"1973","male","Takashi Takeuchi")',
		'INSERT INTO main_creator(creatorID,birthday,gender,name) VALUES (11,"1973","male","Ei Aoki")',
		'INSERT INTO main_creator(creatorID,birthday,gender,name) VALUES (12,"1967","male","Akihiko Yoshida")',
		'INSERT INTO main_creator(creatorID,birthday,gender,name) VALUES (13,"1941","male","Hayao Miyazaki")',
		'INSERT INTO main_creator(creatorID,birthday,gender,name) VALUES (14,"1935","male","Isao Takahata")',
		'INSERT INTO main_creator(creatorID,birthday,gender,name) VALUES (15,"1966","male","Goro Taniguchi")',
		'INSERT INTO main_creator(creatorID,birthday,gender,name) VALUES (16,"1971","male","Hiroyuki Imaishi")',
		'INSERT INTO main_creator(creatorID,birthday,gender,name) VALUES (17,"1966","male","Eiichi Kamagata")',
		'INSERT INTO main_creator(creatorID,birthday,gender,name) VALUES (18,"1971","male","Takami Akai")',
		'INSERT INTO main_creator(creatorID,birthday,gender,name) VALUES (19,"1959","male","Kazuki Nakashima")',
		'INSERT INTO main_creator(creatorID,birthday,gender,name) VALUES (20,"1971","male","Kurasumi Sunayama")',
		'INSERT INTO main_creator(creatorID,birthday,gender,name) VALUES (21,"1961","male","Noriyuki Abe")',
		'INSERT INTO main_creator(creatorID,birthday,gender,name) VALUES (22,"1995","male","Colin Chan")',
	]

	i = 0
	for contents in creatorInsert:
		cursor.execute(str(creatorInsert[i]))
		i+=1
		result = cursor.fetchall()

	# CREATE TABLE main_license(
	  # contentID INT PRIMARY KEY,
	  # studio    VARCHAR(255),
	  # publisher VARCHAR(255),
	  # FOREIGN KEY (studio) references main_studio(studio) ON DELETE NO ACTION,
	  # FOREIGN KEY (contentID) references main_content(contentID) ON DELETE CASCADE
	# );
	# Inserting data into License table
	# Note: foreign keys in django automatically get appended with _id after the variable name
	licenseInsert = [
		'INSERT INTO main_license(contentID_id,studio_id,publisher) VALUES (0,"White Fox","Funimation")',
		'INSERT INTO main_license(contentID_id,studio_id,publisher) VALUES (1,"Studio Pierrot","Funimation")',
		'INSERT INTO main_license(contentID_id,studio_id,publisher) VALUES (2,"Studio 3Hz","Aniplex of America")',
		'INSERT INTO main_license(contentID_id,studio_id,publisher) VALUES (3,"Ufotable","Type-Moon")'
	]

	i = 0
	for contents in licenseInsert:
		cursor.execute(str(licenseInsert[i]))
		i+=1
		result = cursor.fetchall()

	# CREATE TABLE main_hire(
	  # studio  VARCHAR(255) PRIMARY KEY,
	  # creator INT,
	  # FOREIGN KEY(studio) references main_studio(studio) ON DELETE NO ACTION,
	  # FOREIGN KEY (creator) references main_creator(creatorID) ON DELETE NO ACTION
	# );
	# Inserting data into Hire table
	# Note: foreign keys in django automatically get appended with _id after the variable name
	hireInsert = [
		'INSERT INTO main_hire(studio_id,creator_id) VALUES ("White Fox",0)',
		'INSERT INTO main_hire(studio_id,creator_id) VALUES ("White Fox",1)',
		'INSERT INTO main_hire(studio_id,creator_id) VALUES ("White Fox",2)',
		'INSERT INTO main_hire(studio_id,creator_id) VALUES ("Studio Pierrot",3)',
		'INSERT INTO main_hire(studio_id,creator_id) VALUES ("Studio Pierrot",4)',
		'INSERT INTO main_hire(studio_id,creator_id) VALUES ("Studio Pierrot",5)',
		'INSERT INTO main_hire(studio_id,creator_id) VALUES ("Studio 3Hz",6)',
		'INSERT INTO main_hire(studio_id,creator_id) VALUES ("Studio 3Hz",7)',
		'INSERT INTO main_hire(studio_id,creator_id) VALUES ("Studio 3Hz",8)',
		'INSERT INTO main_hire(studio_id,creator_id) VALUES ("Ufotable",9)',
		'INSERT INTO main_hire(studio_id,creator_id) VALUES ("Ufotable",10)',
		'INSERT INTO main_hire(studio_id,creator_id) VALUES ("Ufotable",11)',
		'INSERT INTO main_hire(studio_id,creator_id) VALUES ("Ufotable",12)',
		'INSERT INTO main_hire(studio_id,creator_id) VALUES ("Studio Ghibli", 13)',
		'INSERT INTO main_hire(studio_id,creator_id) VALUES ("Studio Ghibli", 14)',
		'INSERT INTO main_hire(studio_id,creator_id) VALUES ("Sunrise Studio", 15)',
		'INSERT INTO main_hire(studio_id,creator_id) VALUES ("Gainax", 16)',
		'INSERT INTO main_hire(studio_id,creator_id) VALUES ("Gainax", 17)',
		'INSERT INTO main_hire(studio_id,creator_id) VALUES ("Gainax", 18)',
		'INSERT INTO main_hire(studio_id,creator_id) VALUES ("Gainax", 19)',
		'INSERT INTO main_hire(studio_id,creator_id) VALUES ("Gainax", 20)',
		'INSERT INTO main_hire(studio_id,creator_id) VALUES ("Studio Pierrot", 21)',
		'INSERT INTO main_hire(studio_id,creator_id) VALUES ("White Fox", 22)',
		'INSERT INTO main_hire(studio_id,creator_id) VALUES ("Studio Pierrot", 22)',
		'INSERT INTO main_hire(studio_id,creator_id) VALUES ("Studio 3Hz", 22)',
		'INSERT INTO main_hire(studio_id,creator_id) VALUES ("Ufotable", 22)',
		'INSERT INTO main_hire(studio_id,creator_id) VALUES ("Studio Ghibli", 22)',
		'INSERT INTO main_hire(studio_id,creator_id) VALUES ("Sunrise Studio", 22)',
		'INSERT INTO main_hire(studio_id,creator_id) VALUES ("Gainax", 22)',
	]

	i = 0
	for contents in hireInsert:
		cursor.execute(str(hireInsert[i]))
		i+=1
		result = cursor.fetchall()

	# CREATE TABLE main_create(
	  # content INT PRIMARY KEY,
	  # creator INT,
	  # role    VARCHAR(255),
	  # FOREIGN KEY (creator) references main_creator(creatorID) ON DELETE NO ACTION,
	  # FOREIGN KEY (content) references main_content(contentID) ON DELETE CASCADE
	# );
	#Inserting data into Create table
	# Note: foreign keys in django automatically get appended with _id after the variable name
	createInsert = [
		'INSERT INTO main_create(content_id,creator_id,role) VALUES (0,0,"Director")',
		'INSERT INTO main_create(content_id,creator_id,role) VALUES (0,1,"Animator")',
		'INSERT INTO main_create(content_id,creator_id,role) VALUES (0,2,"Author")',
		'INSERT INTO main_create(content_id,creator_id,role) VALUES (1,3,"Author")',
		'INSERT INTO main_create(content_id,creator_id,role) VALUES (1,4,"Director")',
		'INSERT INTO main_create(content_id,creator_id,role) VALUES (1,5,"Animator")',
		'INSERT INTO main_create(content_id,creator_id,role) VALUES (2,6,"Director")',
		'INSERT INTO main_create(content_id,creator_id,role) VALUES (2,7,"Author")',
		'INSERT INTO main_create(content_id,creator_id,role) VALUES (2,8,"Animator")',
		'INSERT INTO main_create(content_id,creator_id,role) VALUES (3,9,"Author")',
		'INSERT INTO main_create(content_id,creator_id,role) VALUES (4,9,"Author")',
		'INSERT INTO main_create(content_id,creator_id,role) VALUES (5,9,"Author")',
		'INSERT INTO main_create(content_id,creator_id,role) VALUES (3,10,"Artist")',
		'INSERT INTO main_create(content_id,creator_id,role) VALUES (5,11,"Director")',
		'INSERT INTO main_create(content_id,creator_id,role) VALUES (5,12,"Animator")',
		'INSERT INTO main_create(content_id,creator_id,role) VALUES (6,13,"Director")',
		'INSERT INTO main_create(content_id,creator_id,role) VALUES (6,14,"Producer")',
		'INSERT INTO main_create(content_id,creator_id,role) VALUES (7,15,"Director")',
		'INSERT INTO main_create(content_id,creator_id,role) VALUES (8,19,"Writer")',
		'INSERT INTO main_create(content_id,creator_id,role) VALUES (9,20,"Writer")',
		'INSERT INTO main_create(content_id,creator_id,role) VALUES (10,16,"Director")',
		'INSERT INTO main_create(content_id,creator_id,role) VALUES (10,17,"Producer")',
		'INSERT INTO main_create(content_id,creator_id,role) VALUES (10,18,"Producer")',
		'INSERT INTO main_create(content_id,creator_id,role) VALUES (11,21,"Director")',
	]

	i = 0
	for contents in createInsert:
		cursor.execute(str(createInsert[i]))
		i+=1
		result = cursor.fetchall()

	# CREATE TABLE VolumeSeason(
		# contentID INT PRIMARY KEY, 
		# num       INT PRIMARY KEY,
		# title     VARCHAR(255),
		# FOREIGN KEY (contentID) REFERENCES main_content(contentID) ON DELETE CASCADE
	# );
	# Inserting data into VolumeSeason table
	# Note: foreign keys in django automatically get appended with _id after the variable name
	volumeSeasonInsert = [
		'INSERT INTO main_volumeSeason(contentID_id,num,title) VALUES (0,1,"Steins;Gate 0")',
		'INSERT INTO main_volumeSeason(contentID_id,num,title) VALUES (1,3,"Tokyo Ghoul:re")',
		'INSERT INTO main_volumeSeason(contentID_id,num,title) VALUES (2,4,"Sword Art Online Alternative: Gun Gale Online")',
		'INSERT INTO main_volumeSeason(contentID_id,num,title) VALUES (5,1,"Season 1")',
		'INSERT INTO main_volumeSeason(contentID_id,num,title) VALUES (5,2,"Season 2")',
		'INSERT INTO main_volumeSeason(contentID_id,num,title) VALUES (5,3,"Season 3")',
		'INSERT INTO main_volumeSeason(contentID_id,num,title) VALUES (7,1,"Lelouch of the Rebellion")',
		'INSERT INTO main_volumeSeason(contentID_id,num,title) VALUES (7,2,"Code Geass: Lelouch of the Rebellion R2")',

		'INSERT INTO main_volumeSeason(contentID_id,num,title) VALUES (8,1,"Volume 1")',
		'INSERT INTO main_volumeSeason(contentID_id,num,title) VALUES (8,2,"Volume 2")',
		'INSERT INTO main_volumeSeason(contentID_id,num,title) VALUES (8,3,"Volume 3")',
		'INSERT INTO main_volumeSeason(contentID_id,num,title) VALUES (8,4,"Volume 4")',
		'INSERT INTO main_volumeSeason(contentID_id,num,title) VALUES (8,5,"Volume 5")',
		'INSERT INTO main_volumeSeason(contentID_id,num,title) VALUES (8,6,"Volume 6")',
		'INSERT INTO main_volumeSeason(contentID_id,num,title) VALUES (8,7,"Volume 7")',
		'INSERT INTO main_volumeSeason(contentID_id,num,title) VALUES (8,8,"Volume 8")',
		'INSERT INTO main_volumeSeason(contentID_id,num,title) VALUES (8,9,"Volume 9")',
		'INSERT INTO main_volumeSeason(contentID_id,num,title) VALUES (8,10,"Volume 10")',
		'INSERT INTO main_volumeSeason(contentID_id,num,title) VALUES (8,11,"Volume 11")',
		'INSERT INTO main_volumeSeason(contentID_id,num,title) VALUES (8,12,"Volume 12")',
		'INSERT INTO main_volumeSeason(contentID_id,num,title) VALUES (8,13,"Volume 13")',
		'INSERT INTO main_volumeSeason(contentID_id,num,title) VALUES (8,14,"Volume 14")',
		'INSERT INTO main_volumeSeason(contentID_id,num,title) VALUES (8,15,"Volume 15")',
		'INSERT INTO main_volumeSeason(contentID_id,num,title) VALUES (8,16,"Volume 16")',
		'INSERT INTO main_volumeSeason(contentID_id,num,title) VALUES (8,17,"Volume 17")',
		'INSERT INTO main_volumeSeason(contentID_id,num,title) VALUES (8,18,"Volume 18")',
		'INSERT INTO main_volumeSeason(contentID_id,num,title) VALUES (8,19,"Volume 19")',
		'INSERT INTO main_volumeSeason(contentID_id,num,title) VALUES (8,20,"Volume 20")',
		'INSERT INTO main_volumeSeason(contentID_id,num,title) VALUES (8,21,"Volume 21")',
		'INSERT INTO main_volumeSeason(contentID_id,num,title) VALUES (8,22,"Volume 22")',
		'INSERT INTO main_volumeSeason(contentID_id,num,title) VALUES (8,23,"Volume 23")',
		'INSERT INTO main_volumeSeason(contentID_id,num,title) VALUES (8,24,"Volume 24")',
		'INSERT INTO main_volumeSeason(contentID_id,num,title) VALUES (8,25,"Volume 25")',

		'INSERT INTO main_volumeSeason(contentID_id,num,title) VALUES (9,1,"Volume 1")',
		'INSERT INTO main_volumeSeason(contentID_id,num,title) VALUES (9,2,"Volume 2")',
		'INSERT INTO main_volumeSeason(contentID_id,num,title) VALUES (9,3,"Volume 3")',
		'INSERT INTO main_volumeSeason(contentID_id,num,title) VALUES (9,4,"Volume 4")',
		'INSERT INTO main_volumeSeason(contentID_id,num,title) VALUES (10,1,"Season 1")',

		'INSERT INTO main_volumeSeason(contentID_id,num,title) VALUES (11,1,"Season 1: The Substitute")',
		'INSERT INTO main_volumeSeason(contentID_id,num,title) VALUES (11,2,"Season 2: Soul Society - Entry")',
		'INSERT INTO main_volumeSeason(contentID_id,num,title) VALUES (11,3,"Season 3: Soul Society - The Rescue")',
		'INSERT INTO main_volumeSeason(contentID_id,num,title) VALUES (11,4,"Season 4: The Bount")',
		'INSERT INTO main_volumeSeason(contentID_id,num,title) VALUES (11,5,"Season 5: The Assault")',
		'INSERT INTO main_volumeSeason(contentID_id,num,title) VALUES (11,6,"Season 6: The Arrancar")',
		'INSERT INTO main_volumeSeason(contentID_id,num,title) VALUES (11,7,"Season 7: The Arrancar Part 2")',
		'INSERT INTO main_volumeSeason(contentID_id,num,title) VALUES (11,8,"Season 8: The Arrancar Part 3")',
		'INSERT INTO main_volumeSeason(contentID_id,num,title) VALUES (11,9,"Season 9: The New Captain Shusuke Amagai")',
		'INSERT INTO main_volumeSeason(contentID_id,num,title) VALUES (11,10,"Season 10: The Arrancar Part 4")',
		'INSERT INTO main_volumeSeason(contentID_id,num,title) VALUES (11,11,"Season 11: The Past")',
		'INSERT INTO main_volumeSeason(contentID_id,num,title) VALUES (11,12,"Season 12: The Arrancar Part 5")',
		'INSERT INTO main_volumeSeason(contentID_id,num,title) VALUES (11,13,"Season 13: Zanpakuto")',
		'INSERT INTO main_volumeSeason(contentID_id,num,title) VALUES (11,14,"Season 14: The Arrancar Part 6")',
		'INSERT INTO main_volumeSeason(contentID_id,num,title) VALUES (11,15,"Season 15: Gotei 13 Invading Army")',
		'INSERT INTO main_volumeSeason(contentID_id,num,title) VALUES (11,16,"Season 16: The Lost Agent")',
	]

	i = 0
	for contents in volumeSeasonInsert:
		cursor.execute(str(volumeSeasonInsert[i]))
		i+=1
		result = cursor.fetchall()

	# CREATE TABLE main_favoritecontent(
	  # userID VARCHAR(255),
	  # contentID INT,
	  # PRIMARY KEY (userID, ContentID), 
	  # FOREIGN KEY (userID) REFERENCES Users (userID) ON DELETE NO ACTION,
	  # FOREIGN KEY (contentID) REFERENCES main_content(contentID) ON DELETE NO ACTION
	# );
	# Inserting data into FavoriteContent table
	# Note: foreign keys in django automatically get appended with _id after the variable name
	favoriteContentInsert = ['INSERT INTO main_favoritecontent(userID_id,contentID_id) VALUES ("eton",0)',
							'INSERT INTO main_favoritecontent(userID_id,contentID_id) VALUES ("colin",1)',
							'INSERT INTO main_favoritecontent(userID_id,contentID_id) VALUES ("linda",1)',
							'INSERT INTO main_favoritecontent(userID_id,contentID_id) VALUES ("scott",3)',
							'INSERT INTO main_favoritecontent(userID_id,contentID_id) VALUES ("test",5)']

	i = 0
	for contents in favoriteContentInsert:
		cursor.execute(str(favoriteContentInsert[i]))
		i+=1
		result = cursor.fetchall()

