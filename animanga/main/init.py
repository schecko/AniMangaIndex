from main.models import *

def init_database():
	
	# CREATE TABLE User(
	  # userID     INT PRIMARY KEY,
	  # privileges INT,
	  # password   VARCHAR(255),
	  # email      VARCHAR(255)
	# );
	#Inserting data into User table
	User.objects.raw('INSERT INTO User(userID,privileges,password,email) VALUES (0,0,1995,"etonk@sfu.ca")')
	User.objects.raw('INSERT INTO User(userID,privileges,password,email) VALUES (1,1,123,"colinc@sfu.ca")')
	User.objects.raw('INSERT INTO User(userID,privileges,password,email) VALUES (2,1,123,"lindaj@sfu.ca")')
	User.objects.raw('INSERT INTO User(userID,privileges,password,email) VALUES (3,1,123,"scottc@sfu.ca")')
	User.objects.raw('INSERT INTO User(userID,privileges,password,email) VALUES (4,0,123,"test@sfu.ca")')
	
	# CREATE TABLE Studio(
	  # name    VARCHAR(255) PRIMARY KEY,
	  # founded DATE
	# );
	#Inserting data into Studio table
	Studio.objects.raw('INSERT INTO Studio(name,founded) VALUES ("White Fox","2007-01-01")')
	Studio.objects.raw('INSERT INTO Studio(name,founded) VALUES ("Studio Pierrot","1979-01-01")')
	Studio.objects.raw('INSERT INTO Studio(name,founded) VALUES ("Studio 3Hz","2013-01-01")')
	Studio.objects.raw('INSERT INTO Studio(name,founded) VALUES ("Ufotable","1997-01-01")')
	
	# CREATE TABLE Content(
	  # contentID INTPRIMARY KEY,
	  # type      VARCHAR(255),
	  # title     VARCHAR(255),
	  # complete  INT,
	  # rating    INT,
	  # date      DATE,
	  # genre     VARCHAR(255),
	  # source    VARCHAR(255)
	# );
	#Inserting data into Content table
	Content.objects.raw('INSERT INTO Content(contentID,type,title,complete,rating,date,genre,source) VALUES (0,"Anime","Steins;Gate",1,9,"2018-04-12","Mystery","Manga")')
	Content.objects.raw('INSERT INTO Content(contentID,type,title,complete,rating,date,genre,source) VALUES (1,"Anime","Tokyo Ghoul",1,7,"2018-04-03","Action","Manga")')
	Content.objects.raw('INSERT INTO Content(contentID,type,title,complete,rating,date,genre,source) VALUES (2,"Anime","Sword Art Online",0,7,"2018-04-08","Fantasy","Book")')
	Content.objects.raw('INSERT INTO Content(contentID,type,title,complete,rating,date,genre,source) VALUES (3,"Manga","Fate/Zero",1,8,"2010-12-29","Action","Book")')
	Content.objects.raw('INSERT INTO Content(contentID,type,title,complete,rating,date,genre,source) VALUES (4,"Book","Fate/Zero",1,7,"2006-12-29","Action",NULL)')
	Content.objects.raw('INSERT INTO Content(contentID,type,title,complete,rating,date,genre,source) VALUES (5,"Anime","Fate/Zero",1,9,"2011-10-01","Action","Manga")')
	
	# CREATE TABLE FavoriteContent(
	  # userID INT,
	  # contentID INT,
	  # PRIMARY KEY (userID, ContentID), 
	  # FOREIGN KEY (userID) REFERENCES Users (userID),
	  # FOREIGN KEY (contentID) REFERENCES Content(contentID)
	# );
	#Inserting data into FavoriteContent table
	Studio.objects.raw('INSERT INTO FavoriteContent(userID,contentID) VALUES (0,0)')
	Studio.objects.raw('INSERT INTO FavoriteContent(userID,contentID) VALUES (1,1)')
	Studio.objects.raw('INSERT INTO FavoriteContent(userID,contentID) VALUES (2,1)')
	Studio.objects.raw('INSERT INTO FavoriteContent(userID,contentID) VALUES (3,3)')
	Studio.objects.raw('INSERT INTO FavoriteContent(userID,contentID) VALUES (4,5)')
	
	# CREATE TABLE Creator(
	  # creatorID INT PRIMARY KEY,
	  # birthday  DATE,
	  # gender    INT,
	  # name      VARCHAR(255)
	# );
	#Inserting data into Creator table
	Creator.objects.raw('INSERT INTO Creator(creatorID,birthday,gender,name) VALUES (0,"1971-01-02",0,"Kenichi Kawamura")')
	Creator.objects.raw('INSERT INTO Creator(creatorID,birthday,gender,name) VALUES (1,"1969-01-01",0,"Jukki Hanada")')
	Creator.objects.raw('INSERT INTO Creator(creatorID,birthday,gender,name) VALUES (2,"1970-07-03",0,"Chiyomaru Shikura")')
	Creator.objects.raw('INSERT INTO Creator(creatorID,birthday,gender,name) VALUES (3,"1985-12-28",0,"Sui Ishida")')
	Creator.objects.raw('INSERT INTO Creator(creatorID,birthday,gender,name) VALUES (4,"1978-06-22",0,"Shuhei Morita")')
	Creator.objects.raw('INSERT INTO Creator(creatorID,birthday,gender,name) VALUES (5,"1980-07-24",0,"Chuji Mikasano")')
	Creator.objects.raw('INSERT INTO Creator(creatorID,birthday,gender,name) VALUES (6,"1974-06-29",0,"Masayuki Sakoi")')
	Creator.objects.raw('INSERT INTO Creator(creatorID,birthday,gender,name) VALUES (7,"1972-01-01",0,"Keiichi Sigsawa")')
	Creator.objects.raw('INSERT INTO Creator(creatorID,birthday,gender,name) VALUES (8,"1968-03-29",0,"Yosuke Kuroda")')
	Creator.objects.raw('INSERT INTO Creator(creatorID,birthday,gender,name) VALUES (9,"1972-12-20",0,"Gen Urobuchi")')
	Creator.objects.raw('INSERT INTO Creator(creatorID,birthday,gender,name) VALUES (10,"1973-08-28",0,"Takashi Takeuchi")')
	Creator.objects.raw('INSERT INTO Creator(creatorID,birthday,gender,name) VALUES (11,"1973-01-20",0,"Ei Aoki")')
	Creator.objects.raw('INSERT INTO Creator(creatorID,birthday,gender,name) VALUES (12,"1967-02-15",0,"Akihiko Yoshida")')
	
	# CREATE TABLE Licenses(
	  # contentID INT PRIMARY KEY,
	  # studio    VARCHAR(255),
	  # publisher VARCHAR(255),
	  # FOREIGN KEY (studio) references Studio(studio),
	  # FOREIGN KEY (contentID) references Content(contentID)

	# );
	#Inserting data into Licenses table
	Licenses.objects.raw('INSERT INTO Licenses(contentID,studio,publisher) VALUES (0,"White Fox","Funimation"")')
	Licenses.objects.raw('INSERT INTO Licenses(contentID,studio,publisher) VALUES (1,"Studio Pierrot","Funimation"")')
	Licenses.objects.raw('INSERT INTO Licenses(contentID,studio,publisher) VALUES (2,"Studio 3Hz","Aniplex of America"")')
	Licenses.objects.raw('INSERT INTO Licenses(contentID,studio,publisher) VALUES (3,"Ufotable","Type-Moon"")')
	
	# CREATE TABLE Hires(
	  # studio  VARCHAR(255) PRIMARY KEY,
	  # creator INT,
	  # FOREIGN KEY(studio) references Studio(studio),
	  # FOREIGN KEY (creator) references Creator(creator)
	# );
	#Inserting data into Hires table
	Hires.objects.raw('INSERT INTO Hires(studio,creator) VALUES ("White Fox",0)')
	Hires.objects.raw('INSERT INTO Hires(studio,creator) VALUES ("White Fox",1)')
	Hires.objects.raw('INSERT INTO Hires(studio,creator) VALUES ("White Fox",2)')
	Hires.objects.raw('INSERT INTO Hires(studio,creator) VALUES ("Studio Pierrot",3)')
	Hires.objects.raw('INSERT INTO Hires(studio,creator) VALUES ("Studio Pierrot",4)')
	Hires.objects.raw('INSERT INTO Hires(studio,creator) VALUES ("Studio Pierrot",5)')
	Hires.objects.raw('INSERT INTO Hires(studio,creator) VALUES ("Studio 3Hz",6)')
	Hires.objects.raw('INSERT INTO Hires(studio,creator) VALUES ("Studio 3Hz",7)')
	Hires.objects.raw('INSERT INTO Hires(studio,creator) VALUES ("Studio 3Hz",8)')
	Hires.objects.raw('INSERT INTO Hires(studio,creator) VALUES ("Ufotable",9)')
	Hires.objects.raw('INSERT INTO Hires(studio,creator) VALUES ("Ufotable",10)')
	Hires.objects.raw('INSERT INTO Hires(studio,creator) VALUES ("Ufotable",11)')
	Hires.objects.raw('INSERT INTO Hires(studio,creator) VALUES ("Ufotable",12)')
	
	# CREATE TABLE Creates(
	  # content INT PRIMARY KEY,
	  # creator INT,
	  # role    VARCHAR(255),
	  # FOREIGN KEY (creator) references Creator(creator),
	  # FOREIGN KEY (content) references Content(content)
	# );
	#Inserting data into Creates table
	Creates.objects.raw('INSERT INTO Creates(content,creator,role) VALUES (0,0,"Director")')
	Creates.objects.raw('INSERT INTO Creates(content,creator,role) VALUES (0,1,"Animator")')
	Creates.objects.raw('INSERT INTO Creates(content,creator,role) VALUES (0,2,"Author")')
	Creates.objects.raw('INSERT INTO Creates(content,creator,role) VALUES (1,3,"Author")')
	Creates.objects.raw('INSERT INTO Creates(content,creator,role) VALUES (1,4,"Director")')
	Creates.objects.raw('INSERT INTO Creates(content,creator,role) VALUES (1,5,"Animator")')
	Creates.objects.raw('INSERT INTO Creates(content,creator,role) VALUES (2,6,"Director")')
	Creates.objects.raw('INSERT INTO Creates(content,creator,role) VALUES (2,7,"Author")')
	Creates.objects.raw('INSERT INTO Creates(content,creator,role) VALUES (2,8,"Animator")')
	Creates.objects.raw('INSERT INTO Creates(content,creator,role) VALUES (3,9,"Author")')
	Creates.objects.raw('INSERT INTO Creates(content,creator,role) VALUES (4,9,"Author")')
	Creates.objects.raw('INSERT INTO Creates(content,creator,role) VALUES (5,9,"Author")')
	Creates.objects.raw('INSERT INTO Creates(content,creator,role) VALUES (3,10,"Artist")')
	Creates.objects.raw('INSERT INTO Creates(content,creator,role) VALUES (5,11,"Director")')
	Creates.objects.raw('INSERT INTO Creates(content,creator,role) VALUES (5,12,"Animator")')
	
	# CREATE TABLE VolumeSeason(
		# contentID INT PRIMARY KEY, 
		# num       INT,
		# title     VARCHAR(255),
		# FOREIGN KEY (contentID) REFERENCES Content(contentID)
	# );
	#Inserting data into VolumeSeason table
	VolumeSeason.objects.raw('INSERT INTO VolumeSeason(contentID,num,title) VALUES (0,1,"Steins;Gate 0")')
	VolumeSeason.objects.raw('INSERT INTO VolumeSeason(contentID,num,title) VALUES (1,3,"Tokyo Ghoul:re")')
	VolumeSeason.objects.raw('INSERT INTO VolumeSeason(contentID,num,title) VALUES (2,4,"Sword Art Online Alternative: Gun Gale Online")')
	VolumeSeason.objects.raw('INSERT INTO VolumeSeason(contentID,num,title) VALUES (3,0,"Fate/Zero")')
	VolumeSeason.objects.raw('INSERT INTO VolumeSeason(contentID,num,title) VALUES (4,5,"Fate/Zero")')
	VolumeSeason.objects.raw('INSERT INTO VolumeSeason(contentID,num,title) VALUES (5,1,"Fate/Zero")')
	