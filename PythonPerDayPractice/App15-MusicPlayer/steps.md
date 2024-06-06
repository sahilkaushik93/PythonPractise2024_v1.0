## Steps to build a React-Django Framework

* In vs code need extensions like: es7 react, es6 javascript, django, prettier etc.
* pip install django djangorestframework
* django-admin startproject music_controller
* cd .\music_controller\
* django-admin startapp api
* go to "music controller/settings.py" -> INSTALLED_APPS -> add "api".
* Add urls.py in api & edit urls.py in music_controller
* python manage.py makemigrations
* python manage.py migrate
* python manage.py runserver