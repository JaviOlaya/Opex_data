from django.shortcuts import render
from django.views.generic import(
    ListView,
    DetailView,
    CreateView
)
from .models import Personal
from .models import GastosAdministrativos
from .models import GastosCultivos

class ListaAllEmpleados(ListView):
    template_name="empleados/listaEmpleados.html"
    #La paginación se hace muy fácil
    paginate_by = 1
    model = Personal
    context_object_name = 'listaEmpleados'
    
class ListByArea(ListView):
    template_name="empleados/listaEmpleados_by_area.html"
    # queryset = Personal.objects.filter(
    #     Plantilla = 'Soporte'
    # )
    #Funcion para escribir filtro en un listado por metodo get
    def get_queryset(self):
        
        area = self.kwargs['Plantilla']
        lista = Personal.objects.filter(
        Plantilla = area
        )
        return lista
    
#4Listar los empleados por palabra clave
class ListaEmpleadosByKword(ListView):
    template_name = "empleados/Empleados_kword.html"
    context_object_name ="empleados"
    
    def get_queryset(self):
        print("*******************************")
        palabra_clave = self.request.GET.get('kword','')
        print('=======',palabra_clave)
        lista = Personal.objects.filter(
            Plantilla = palabra_clave
        )
        print('lista resultado: ',lista)
        return lista
    
class IntGastosAdmin(CreateView):
    template_name = 'Gastos/intGastoAdmin.html'
    model=GastosAdministrativos
    fields=('__all__')
    #web a la que tiene que redirigirse al guardar los datos del formulario
    succes_url ="."
    # context_object_name = "Gastos Administrativos"
class IntGastosCultivos(CreateView):
    template_name = 'Gastos/intGastosCultivos.html'
    model=GastosCultivos
    fields=('__all__')
    #web a la que tiene que redirigirse al guardar los datos del formulario
    succes_url ="."    