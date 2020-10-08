from django.urls import path
from . import views

urlpatterns =[
    path('listado/', views.ListaAllEmpleados.as_view()),
    path('listado-by-area/<Plantilla>', views.ListByArea.as_view()),
    path('listado-by-kword/', views.ListaEmpleadosByKword.as_view()),
    path('listado-by-kword/', views.ListaEmpleadosByKword.as_view()),
    path('gastos_admin/', views.IntGastosAdmin.as_view()),
    path('gastos_cultivo/', views.IntGastosCultivos.as_view()),
]