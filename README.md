# AniMangaIndex

# Requirements ( for development )
- the root access
- ubuntu 16.04
- python (at least version 3.x)

# Installation ( for development )
1. open up a terminal, cd to the root of the repository (where this README is)
2. verify your python version
    <br/>python3 --version
3. if the previous command fails:
    <br/>sudo apt-get install python3
4. install the python package manager, pip (give the root password if prompted):
    <br/>sudo apt-get install -y python3-pip
5. install django:
   <br/>pip3 install django
6. move one directory into the repository (the correct destination folder will contain manage.py)
    <br/>cd animanga/
7. build the database
    <br/>python3 manage.py makemigrations
    <br/>python3 manage.py migrate
8. run the server locally
    <br/>python3 manage.py runserver
9. open up your favorite browser
10. go to the following url:
    <br/>http://localhost:8000


# Features:
- Login and create new users on index page
- Login on content page (note: login will return to index (after successful login)
- Admin privileges for specific users
- View content
- View creators
- Various other queries

# Some basic queries and their locations 

NOTE: All links are available through the UI at the index, 
    but they are given here for completeness.

Projection query:
Users can view all available content or creators at the index page
        <br/>--> http://localhost:8000/

Selection query:
Users can query which anime or manga are of a certain age or younger/older.
        <br/>--> http://localhost:8000/selection/

Join query:
Users can view a list of content and their creators.
        <br/>--> http://localhost:8000/?indexQuery=Joined

Aggregation query:
Users can view how many works a creator has worked on.
        <br/>--> http://localhost:8000/create/

Users can also view how many creators worked on the same content.
        <br/>--> http://localhost:8000/contributorcount/

Nested aggregation with group-by:
User can finding creators whose age is younger than the average age of all creators.
        <br/>--> http://127.0.0.1:8000/nested/

Update query:
Users can update the rating of anime or manga (Botton labeled "Change Rating"):
        <br/>--> http://localhost:8000/content/3/
        <br/>NOTE: Going to the index and then clicking on any of the content 
            titles will go to a similar page to the one listed above, any of
            which can have their rating changed. The specific link was chosen at
            random.

Delete query:
Admin can delete anime or manga (Button labeled "Delete this content" when logged in as an admin).
        <br/>--> http://localhost:8000/content/3/
        <br/>NOTE: The user must be logged in as an admin to delete content. At the top of the index is a 
        login button, and the TA may use the login user "admin" with password "123" both without quotes.
        Creating a normal user will not allow the TA to delete content. After logging in, the TA may go 
        to a any content page(the above link is a single example of a content page) and at the
        bottom of the page the button to delete the entry can be found.

Division query:
Find creators that worked in every studio.
        <br/>--> http://localhost:8000/division/

