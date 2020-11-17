from django.shortcuts import render, get_object_or_404
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    TemplateView,
    UpdateView,
    DeleteView,
)
# Create your views here.
from django.shortcuts import render
from aplications.inputapp.models import *
from .models import Page

# Create your views here.

# def page(request, slug):
    
#     page = Page.objects.get(slug=slug)
        
#     return render(request, "pages/page.html",{
#         'title':page.title,
#         "page":page
#     })

class ListProyecto(ListView):
    template_name = "pages/list_proyectos.html"
    paginate_by = 4
    ordering = 'id'
    model = Proyecto

class ListPersonal(ListView):
    template_name = "pages/list_personal.html"
    paginate_by = 4
    ordering = 'id'
    model = Personal

class ListGastoAdministrativo(ListView):
    template_name = "pages/list_g_admin.html"
    paginate_by = 4
    ordering = 'id'
    model = GastoAdministrativo

class ListGastoAdministrativo(ListView):
    template_name = "pages/list_g_admin.html"
    paginate_by = 4
    ordering = 'id'
    model = GastoAdministrativo    

class ListElectricCost(ListView):
    template_name="pages/list_g_electro.html"
    model = GastoElectrico 
    paginate_by = 4
    ordering = "id"
    context_object_name ="Electric Cost"
    
class ListGasCost(ListView):
    template_name="pages/list_g_gas.html"
    model = GastoGas
    paginate_by = 4
    ordering = "id"
    context_object_name ="Gas cost"

class ListFertilizerCost(ListView):
    template_name="pages/list_g_fertilizante.html"
    model = GastoFertilizante 
    paginate_by = 4
    ordering = "id"
    context_object_name ="Fertilizer cost"
    
class ListSubstrateCost(ListView):
    template_name="pages/list_g_substrato.html"
    model = GastoSubstrato 
    paginate_by = 4
    ordering = "id"
    context_object_name ="Substrate List"
    
class ListShippingCost(ListView):
    template_name="pages/list_g_envio.html"
    model = GastoEnvio
    paginate_by = 4
    ordering = "id"
    context_object_name ="Shipping list"

class ListSeedsCost(ListView):
    template_name="pages/list_g_semillas.html"
    model = GastoSemillas 
    paginate_by = 4
    ordering = "id"
    context_object_name ="Seeds List"

class ListFuelCost(ListView):
    template_name="pages/list_g_combustible.html"
    model = GastoCombustible 
    paginate_by = 4
    ordering = "id"
    context_object_name ="Fuel list"

class ListCleaningCost(ListView):
    template_name="pages/list_g_limpieza.html"
    model = GastoLimpieza 
    paginate_by = 4
    ordering = "id"
    context_object_name ="Cleaning list"
    
    
class ListVariousCost(ListView):
    template_name="pages/list_g_vario.html"
    model = VariosGasto 
    paginate_by = 4
    ordering = "id"
    context_object_name ="List various"

class ListTaxRate(ListView):
    template_name="pages/list_g_taxrate.html"
    model = taxRate
    paginate_by = 4
    ordering = "id"
    context_object_name ="List Tax Rate"
    
class ListMacroeconomicsIndicator(ListView):
    template_name="pages/list_g_macroeconomics.html"
    model = macroeconomicsIndicators
    paginate_by = 4
    ordering = "id"
    context_object_name ="List Macroeconomics Indicators"

    # context_object_name = 'lista'

    # def list_proyecto(request):
        
    #     return render(request,'pages/list_proyectos.html',{
    #         'title':'Listado de Proyectos'
        
    #     })
# def list_personal(request):
#     return render(request,'pages/list_personal.html',{
#         'title':'Listado de gastos de personal'
#     })

# def list_admin(request):
#     return render(request,'pages/list_g_admin.html',{
#         'title':'Listado gastos administrativos'
#     })
# def list_electro(request):
#     return render(request,'pages/list_g_electro.html',{
#         'title':'Listado gastos de electricidad'
#     })
# def list_gas(request):
#     return render(request,'pages/list_g_gas.html',{
#         'title':'Listado gastos de gas'
#     })
# def list_fertilizante(request):
#     return render(request,'pages/list_g_fertilizante.html',{
#         'title':'Listado gastos de fertilizante'
#     })
# def list_substrato(request):
#     return render(request,'pages/list_g_substrato.html',{
#         'title':'Listado gastos de substrato'
#     })
# def list_envio(request):
#     return render(request,'pages/list_g_envio.html',{
#         'title':'Listado gastos de  envíos'
#     })
# def list_remedio(request):
#     return render(request,'pages/list_g_remedio.html',{
#         'title': 'Listado gastos de remedios'
#     })
# def list_semillas(request):
#     return render(request,'pages/list_g_semillas.html',{
#         'title':'Listado gastos de semillas'
#     })
# def list_combustible(request):
#     return render(request,'pages/list_g_combustible.html',{
#         'title':'Listado gastos de combustible'
#     })
# def list_limpieza(request):
#     return render(request,'pages/list_g_limpieza.html',{
#         'title':'Listado gastos de limpieza'        
#     })
# def list_gastovario(request):
#     return render(request,'pages/list_g_vario.html',{
        
#     })