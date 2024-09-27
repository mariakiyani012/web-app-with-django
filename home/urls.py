from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from home import views

urlpatterns = [
    path("", views.index, name='home'),
    path("services", views.services, name='services'),
    path("about", views.about, name='about'),
    path("careers", views.careers, name='careers'),
    path("schedule", views.schedule, name='schedule')
]