from django.urls import path, re_path
from django.contrib import admin

from . import views

urlpatterns = [
    path('', views.home_page_view, name='home_view'),
    path('about-us/', views.aboutUs_page_view, name='aboutUs_view'),
    path('contacts/', views.contacts_page_view, name='contacts_view'),
    path('cosmetology/', views.cosmetology_page_view, name='cosmetology_view'),
    path('haircuting/', views.haircuting_page_view, name='haircuting_view'),
    path('makeup/', views.makeup_page_view, name='makeup_view'),
    path('massage/', views.massage_page_view, name='massage_view'),
    path('nails/', views.nails_page_view, name='nails_view'),
    path('order-parking/', views.order_parking_view, name='order_parking_view'),
    path('projects/', views.our_projects_page_view, name='our_projects_view'),
    path('sales/', views.sales_page_view, name='sales_view'),
    path('services/', views.services_page_view, name='services_view'),
    path('vacancies/', views.vacancies_page_view, name='vacancies_view'),
    path('register/', views.register_page_view, name='register_view'),
    # ____________________________________________________________________________
    path('index/', views.index, name='index'),
    path('cat/<slug:cat>/', views.categories, name='categories'),
    # re_path(r'^archive/(?P<year>[0-9]{3})/', views.archive, name='archive')
    path('category/<int:cat_id>/', views.show_category, name='category')
]