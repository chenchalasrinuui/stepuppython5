from django.urls import path
from . import views
urlpatterns = [
    path('home', views.fnHome),
    path('about', views.fnAbout),
    path('contact', views.fnContact),
]
