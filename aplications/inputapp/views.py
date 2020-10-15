from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from aplications.inputapp.models import *

# Create your views here.
def proyecto_detail(request):
    return render(request,'pages/l.html',{
        'title':'Listado de Proyectos'
    })
def list_personal(request):
    return render(request,'pages/list_personal.html',{
        'title':'Listado de gastos de personal'
    })

def list_admin(request):
    return render(request,'pages/list_g_admin.html',{
        'title':'Listado gastos administrativos'
    })
def list_electro(request):
    return render(request,'pages/list_g_electro.html',{
        'title':'Listado gastos de electricidad'
    })
def list_gas(request):
    return render(request,'pages/list_g_gas.html',{
        'title':'Listado gastos de gas'
    })
def list_fertilizante(request):
    return render(request,'pages/list_g_fertilizante.html',{
        'title':'Listado gastos de fertilizante'
    })
def list_substrato(request):
    return render(request,'pages/list_g_substrato.html',{
        'title':'Listado gastos de substrato'
    })
def list_envio(request):
    return render(request,'pages/list_g_envio.html',{
        'title':'Listado gastos de  envíos'
    })
def list_remedio(request):
    return render(request,'pages/list_g_remedio.html',{
        'title': 'Listado gastos de remedios'
    })
def list_semillas(request):
    return render(request,'pages/list_g_semillas.html',{
        'title':'Listado gastos de semillas'
    })
def list_combustible(request):
    return render(request,'pages/list_g_combustible.html',{
        'title':'Listado gastos de combustible'
    })
def list_limpieza(request):
    return render(request,'pages/list_g_limpieza.html',{
        'title':'Listado gastos de limpieza'        
    })
def list_gastovario(request):
    return render(request,'pages/list_g_vario.html',{
        
    })