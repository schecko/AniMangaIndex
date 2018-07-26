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
    python --version
3. if the version is less than 3:
    sudo add-apt-repository ppa:jonathonf/python-3.6
    sudo apt-get update
    sudo apt-get install python3.6
2. run the following command(give the root password if it asks and reply with 'y' when prompted) :
    sudo apt install python pip
3. 


Pre-testing procedures:
1) delete db.sqlite
2) pyhton manage.py migrate
3) python manage.py runserver
4) Go to index page 127.0.0.1:8000
5) Starting testing

Testing:
Specific function test(query tests):

Done (Test and verified queries):
- Login on index page
- Login on content page (note: login will return to index (after successful login)
- Projection query works
- Selection query works
- Aggregation query works
- Update query (rating) works
- Selete query works
- Division query (colin chan) works

To be implemented (missing queries):
- Join query
- Nested aggregation query
