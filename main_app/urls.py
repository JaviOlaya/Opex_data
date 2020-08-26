from django.urls import path
from . import views

urlpatterns =[
    
    path('', views.portada, name="portada"),
    path('inicio/', views.index, name="inicio"),
    path('register/', views.register_page, name="register"),
    path('login/', views.login_page, name="login"),
]