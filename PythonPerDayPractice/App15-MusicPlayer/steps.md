## Steps to build a React-Django Framework

### Django Backend (api folder)
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
* create your model in models.py
* create serializers.py in api folder to create a json response from models.py


### React FrontEnd (frontend folder)
* install npm -> check by typing "npm" in terminal
* django-admin startapp frontend
* create "frontend/templates", "frontend/static/frontend", "frontend/static/css" & "frontend/static/images", "frontend/src/components"
* npm packages required:
    1. cd <frontend folder> : "npm init -y" : it will generate node module & package structure that we need -> it will generate "package.json"
    2. "npm i webpack webpack-cli --save-dev" : it will install all javascript bundle required.
    3. "npm i @babel/core babel-loader @babel/preset-env @babel/preset-react --save-dev" : to make our E6 code compatible with all browsers 
    4. "npm i react react-dom --save-dev": installing react
    5. "npm install @mui/material @emotion/react @emotion/styled": to style the webpage
    6. "npm install @babel/plugin-proposal-class-properties": to use async & await in javascript
    7. "npm install react-router-dom": will help to write two different pages that we will create in react
    8. "npm install @mui/material @mui/icons-material @emotion/react @emotion/styled": to get icons for webpage
* setup configuration scripts required in webpack & babel
    1. create "frontend/babel.config.json"
    2. create "frontend/webpack.config.json": it will create a bundle of all javascript file and will provide it to webpage as a single bundle containg all .js files.
    3. In "package.json" enter scripts names
* create "src/index.json"
* create "frontend/templates/frontend/index.html"
* edit "frontend/templates/frontend/index.html", "frontend/view.py", "frontend/urls.py" & "music_controller/urls.py"


