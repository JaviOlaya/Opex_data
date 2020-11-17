from django.contrib import admin
from django.urls import path
from . import views

app_name = "mainapp"


urlpatterns = [
    path("inicio/", views.index, name="inicio"),
    path("", views.portada, name="portada"),
    path("registro/", views.register_form, name="registro"),
    path("login/", views.login_form, name="login"),
    path("logout/", views.logout_user, name="logout"),
    path("edit_profile/", views.update_form, name="editProfile")
]