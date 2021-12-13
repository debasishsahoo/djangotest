from django.contrib import admin
from django.urls import path
from foodsite import views

urlpatterns = [
    path('', views.index, name='home'),
    path('home/', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('feature/', views.feature, name='feature'),
    path('chef/', views.chef, name='chef'),
    path('menu/', views.menu, name='menu'),
    path('booking/', views.booking, name='booking'),
    path('contact/', views.contact, name='contact'),
]
