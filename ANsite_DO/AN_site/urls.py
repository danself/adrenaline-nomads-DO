from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name = 'start'),
    path('Home.html', views.home, name = 'home'),
    path('About.html', views.about, name = 'about'),
    path('Contact.html', views.contact, name = "contact"),
]
