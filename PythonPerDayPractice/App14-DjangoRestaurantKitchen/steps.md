## Steps for App 14 - Restaurant Kitchen Web App

* Generating QR Code:-
    1. In qr.py, edit the url in "qrcode.make()" with url where you have hosted your application.
    2. run qr.py, it will generate a qr code for your user.
    3. By scanning this qr code your users can reach to your app directly

* Setting up django app
    1. pip install django
    2. "django-admin startproject mysite ."
    3. "python manage.py startapp restaurant_menu"
    4. go to "mysite/setting.py" -> add your app in "INSTALLED_APPS" list
    5. "python manage.py runserver"

* Creating database model
    1. go to "restaurant_menu/models.py" -> add your model.
    2. "python manage.py makemigrations"
    3. "python manage.py migrate"

* Creating Views, Templates & Admin setup
    1. go to "restaurant_menu/views.py" -> add your views.
    2. create "restaurant_menu/templates" -> "index.html" & "menu_item_detail.html" in it.
    3. connect views.py & templates by mentioning "template_name = <template.html>" in the class.
    4. connect everything with the help of urls: create "restaurant_menu/urls.py" -> add urlpatterns in it. Then in "mysite/urls.py" -> add urlpatterns for connecting restaurant_menu views & templates with django app.

* Context in django
    1. HTML pages need data from views.py to display on web-pages. To get those data in views.py & give it to HTML pages, we require context.
    2. to implement context in django, we require pre-defined method a.k.a "get_context_data()". 
    3. In get_context_data(), we defined "context" dictionary these dict keys can be referred by HTML pages directly using {{ key_name }}.

* Admin Finalisation
    1. go to "restaurant_menu/admin.py" -> create a class for admin.
    2. create super user : "python manage.py createsuperuser" -> give credentials to login into admin.py.
    3. from admin we can add items to be displayed on web-page.

* Displaying data on web-page
    1. 







