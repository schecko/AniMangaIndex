# AniMangaIndex

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
