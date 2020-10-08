from django.urls import path,include
from . import views

urlpatterns =[
    
    path('', views.portada, name="portada"),
    path('inicio', views.index, name="inicio"),
    path('register/', views.register_page, name="register"),
    path('login/', views.login_page, name="login"),
    path('logout/',views.logout_user, name='logout'),
    
]