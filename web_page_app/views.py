from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

from .models import *
from django.contrib.auth.forms import UserCreationForm
# Create your views here.


def home_page_view(request):
    return render(request, 'containers/home_page.html')


def aboutUs_page_view(request):
    return render(request, 'containers/about_usPage.html')


def contacts_page_view(request):
    return render(request, 'containers/contactsPage.html')


def cosmetology_page_view(request):
    return render(request, 'containers/cosmetologyPage.html')


def haircuting_page_view(request):
    return render(request, 'containers/haircutingPage.html')


def makeup_page_view(request):
    return render(request, 'containers/makeupPage.html')


def massage_page_view(request):
    return render(request, 'containers/massagePage.html')


def nails_page_view(request):
    return render(request, 'containers/nailsPage.html')


def order_parking_view(request):
    return render(request, 'containers/orderParking.html')


def our_projects_page_view(request):
    return render(request, 'containers/our_projectsPage.html')


def sales_page_view(request):
    return render(request, 'containers/salesPage.html')


def services_page_view(request):
    return render(request, 'containers/servicesPage.html')


def vacancies_page_view(request):
    return render(request, 'containers/vacanciesPage.html')

def register_page_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home_page_view') # LEAD TO LOGIN!!!
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


# Django docks ____________________________________________________________________

menu = ['About syte', 'add news', 'callback answer', 'Come in']

def index(request):
    posts = Women.objects.all()
    cats = Category.objects.all()
    context = {'title': 'IndexPage', 
               'menu': menu, 
               'posts': posts,
               'title': "Main page",
               'cat_selected': 0
               }

    return render(request, 'containers/indexPage.html', context=context)

def categories(request, cat):
    if request.GET:
        print(request.POST)

    return HttpResponse(f'Categories. with cats {cat}')


def archive(request, year):
    return HttpResponse(f'<h1>Archive about cities</h1><p>{year}</p>')

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Page not found</h1>')

def show_category(request, cat_id):
    return HttpResponse(f"Отображение категории с id = {cat_id}")