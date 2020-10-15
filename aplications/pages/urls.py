from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("lista/", views.list, name="lista_proyectos"),
]