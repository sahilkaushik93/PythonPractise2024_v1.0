## Django Steps

* In Terminal: "pip install django"

* In Terminal: "django-admin startproject mysite ." It will create folder structure in root directory so better first change directory in termainal using "cd" command, in which you want to create folder strucuture and then run above command.

* 2nd step will create a folder "mysite" containing __init__.py, asgi.py, settings.py, urls.py, wsgi.py. It will create manage.py also.

* In Terminal: "python manage.py startapp job_application" It will create a folder job_application containing few files. Here, it is basically running manage.py file that expects few parameter like "startapp" & "your app name" for e.g. in our case it's "job_application"

* Here, mysite folder files & manage.py is one project. A project can contain multiple apps like "job_application".

* Go to mysite -> settings.py -> "INSTALLED_APPS" In Application definition Section. Add 'job_application' in "INSTALLED_APPS". 

* In Terminal type: "python manage.py runserver" command to run you django website.

* Django Development follows a bottom-up approach i.e. first develop database then backend then front-end.

* Database Models:
    1. For Database models: Go to job_application -> models.py -> add your database model definition in it.

    2. Create database migrations: "python manage.py makemigrations". This command will create 0001_initial.py file in "./job_applications/migrations" folder (Make sure that you have added "job_application" in "./mysite/settings.py/INSTALLED_APPS"). By above command, "Form" class defined in models.py is interpereted in python code required by django.

    3. The "0001_initial.py" is a kind of middle man b/w "Form" class & dbsqlite3 present in root directory.

    4. Right now you won't be able to see changes in db. To apply changes in db, use following command: "python manage.py migrate". This means that a table with same schema defined in "models.py/Form" have been generated in dbsqlite3.

* Creating View & Templates:
    1. Go to "job_application/views.py" -> create your views
    2. For templates like "index.html". Either you can specify location where you are putting these templates in "mysite/settings.py/TEMPLATES/DIRS" or we can create a folder called "templates" in "job_application" and save all files like "index.html" inside it.
    3. In flask we give decorators "@app.route("/")" to connect functions with a specific url/endpoint but in Django we create a urls.py file to connect all functions created in views to webpage.
    4. Create a "urls.py" in "job_application" -> add "urlpatterns" in it of all the pages you want to add.
    5. Go to mysite -> urls.py -> urlpatterns -> add urlpatterns of all the pages under admin path.

* Creating a Form model:
    1. A Form model is suppose to help us update the db by fetching reponse from users. Users will generate a POST request that will save data in form model & thus in end db will be updated.
    2. Create forms.py in same directory as views.py (in job_application folder). 
    3. forms.py is for Application Form & models.py is for database.
    4. In views.py: create all variables storing user response requests values"form.cleaned_data['first_name']". Here "first_name" is the value provided in "index.html" to first name input field.
    5. With this we will have users response that he/she would provide via web-page inside the variables "first_name", "last_name", "date", "occupation" & "email" defined in "views.py/index()".

*  Storing data in database:
    1. Import Db model in views: from .models import Form (Where we have defined our DB schema).
    2. If it is an input fetched from index page add few lines in index function to save in db.
    3. "Form.objects.create()" function will help to interact with db & it will create the data replica into dbsqlite3.

* Displaying Success message on front-end:
    1. "from django.contrib import messages" in views.py.
    2. use messages.success() to dosplay messages

* Sending an email of confirmation
    1. "from django.coore.mail import EmailMessage" in views.py.
    2. In mysite/settings -> under "# Default primary key field type" section -> add: EMAIL_BACKEND, EMAIL_HOST, EMAIL_HOST_USER, EMAIL_HOST_PASSWORD, EMAIL_PORT, EMAIL_USER_TLS.
    3.   In view.py