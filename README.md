# AniMangaIndex

##
# Install instructions
##

Before starting, here are some assumptions these instructions make:
    - the TA has root access to their machine (CSIL machines will not work because of this)
    - the TA is using ubuntu 16.04
    - as the TA is using ubuntu, they already have python installed (at least version 3.x)
    - the TA already has our files located somewhere on their machine
    - the TA has some knowledge of bash

1. open up a terminal, cd to the root of the repository (where this README is)
2. verify your python version
    python3 --version
3. if the previous command fails:
    sudo apt-get install python3
3. install the python package manager, pip (give the root password if prompted) :
    sudo apt-get install -y python3-pip
4. install django:
    pip3 install django
5. move one directory into the repository (the correct destination folder will contain manage.py)
    cd animanga/
6. build the database
    python3 manage.py makemigrations
    python3 manage.py migrate
7. run the server locally
    python3 manage.py runserver
8. open up your favorite browser (we used chrome to test and develop)
9. go to the following url:
    http://localhost:8000

##
# Features:
##
- Login and create new users on index page
- Login on content page (note: login will return to index (after successful login)
- admin privileges for specific users
- view content
- view creators
- various other queries

## 
# Required Queries and their Locations
## 

NOTE: All links are available through the UI at the index, 
    but they are given here for completeness.

Projection query:
Users can view all available content or creators at the index page
        --> http://localhost:8000/

Selection query:
Users can query which anime or manga are of a certain age or younger/older.
        --> http://localhost:8000/selection/

Join query:
Users can view a list of content and their creators.
        --> http://localhost:8000/?indexQuery=Joined

Aggregation query:
Users can view how many works a creator has worked on.
        --> http://localhost:8000/create/
Users can also view how many creators worked on the same content.
        --> http://localhost:8000/contributorcount/

Nested aggregation with group-by:
User can finding creators whose age is younger than the average age of all creators.
        --> http://127.0.0.1:8000/nested/

Update query:
Users can update the rating of anime or manga (Botton labeled "Change Rating"):
        --> http://localhost:8000/content/3/
        NOTE: Going to the index and then clicking on any of the content 
            titles will go to a similar page to the one listed above, any of
            which can have their rating changed. The specific link was chosen at
            random.

Delete query:
Admin can delete anime or manga (Button labeled "Delete this content" when logged in as an admin).
        --> http://localhost:8000/content/3/
        NOTE: The user must be logged in as an admin to delete content. At the top of the index is a 
        login button, and the TA may use the login user "admin" with password "123" both without quotes.
        Creating a normal user will not allow the TA to delete content. After logging in, the TA may go 
        to a any content page(the above link is a single example of a content page) and at the
        bottom of the page the button to delete the entry can be found.

Division query:
Find creators that worked in every studio.
        --> http://localhost:8000/division/

##
# Dev procedures ( not for the TA ):
## 
1) delete db.sqlite3
2) python manage.py migrate
3) python manage.py runserver
4) Go to index page 127.0.0.1:8000
5) Starting testing