@echo off
REM echo Starting AniManga's Project
REM C:
REM cd C:\Users\Eton\Envs\AniMangaIndex
REM workon cmpt354

echo Start Server
python manage.py migrate
python manage.py sqlmigrate main 0001

python manage.py loaddata fixtures/init_user.json
python manage.py loaddata fixtures/init_studio.json
python manage.py loaddata fixtures/init_content.json
python manage.py loaddata fixtures/init_favoritecontent.json
python manage.py loaddata fixtures/init_creator.json
python manage.py loaddata fixtures/init_creates.json
python manage.py loaddata fixtures/init_hires.json
python manage.py loaddata fixtures/init_licenses.json
python manage.py loaddata fixtures/init_volumeseason.json

python manage.py runserver
