from django.shortcuts import render
from .forms import ApplicationForm # ".forms" refer the local file, "forms" refer the file in root directory

# Create your views here.
def index(request):
    '''
    Here, instead of "render_template"(like in flask) 
    we use "render"(in Django).

    '''
    if request.method == ['GET', 'POST']:
        form = ApplicationForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            date = form.cleaned_data['date']
            occupation = form.cleaned_data['occupation']
            print(first_name)
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")