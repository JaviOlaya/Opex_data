from django.shortcuts import render, get_object_or_404,HttpResponse
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    TemplateView,
    UpdateView,
    DeleteView,

)
from .models import *
from django.db.models import Q 
from .forms import FormProyecto
# Create your views here.


# Create your views here.


class ProyectosCreateView(CreateView):
    template_name = 'inputapp/create_full_proyecto.html'
    model = Proyecto
    fields = '__all__'
    #form_class = FormProyecto
    success_url = reverse_lazy('inputapp:correcto')
    
    def form_valid(self, form):
            #logica del proceso
        proyecto = form.save(commit=False)
        proyecto.save()
        return super(ProyectosCreateView, self).form_valid(form)
    
class ProyectosUpdateView(UpdateView):
    model = Proyecto
    template_name = "inputapp/update_proyectos.html"
    fields = '__all__'
    success_url = reverse_lazy('inputapp:correcto')
    
    def post(self, request, *args, **kwargs):
        self.object  = self.get_object()
        print("*******METODO POST*******")
        print("=========================")
        return super().post(request, *args, **kwargs)
      
    def form_valid(self, form):
        #logica del proceso
        print("*******VALIDACION********")
        print("*************************")
        return super(ProyectosUpdateView, self).form_valid(form)
   
class ProyectosDeleteView(DeleteView):
    model = Proyecto
    template_name = "inputapp/borrar_proyecto.html"
    success_url = reverse_lazy('inputapp:correcto') 

class ListPersonal(ListView):
    template_name="pages/list_personal.html"
    model = Personal 
    paginate_by = 4
    ordering = "nombre"
    context_object_name ="Staff List"

class PersonalCreateView(CreateView):
    template_name = 'inputapp/create_g_personal.html'
    model = Personal
    fields = '__all__'
    success_url = 'reverse_lazy(inputapp:correcto)'
    
    def form_valid(self, form):
            #logica del proceso
        personal = form.save(commit=False)
        personal.save()
        return super(PersonalCreateView, self).form_valid(form)
    
class PersonalUpdateView(UpdateView):
    model = Personal
    template_name = "inputapp/update_personal.html"
    model = Personal
    fields = '__all__'
    success_url = reverse_lazy('inputapp:correcto')
    
    def post(self, request, *args, **kwargs):
        self.object  = self.get_object()
        print("*******METODO POST*******")
        print("=========================")
        return super().post(request, *args, **kwargs)
      
    def form_valid(self, form):
        #logica del proceso
        print("*******VALIDACION********")
        print("*************************")
        return super(PersonalUpdateView, self).form_valid(form)
   
class PersonalDeleteView(DeleteView):
    model = Personal
    template_name = "inputapp/borrar_personal.html"
    success_url = reverse_lazy('inputapp:correcto')     


class ListAdminCost(ListView):
    template_name="pages/list_g_admin.html"
    model = GastoAdministrativo
    paginate_by = 4
    ordering = "nombre"
    context_object_name ="Proyectos"

class AdminCostCreateView(CreateView):
    template_name = 'inputapp/create_g_admin.html'
    model = GastoAdministrativo
    fields = '__all__'
    success_url = 'reverse_lazy(inputapp:correcto)'
    
    def form_valid(self, form):
            #logica del proceso
        gasto_admin = form.save(commit=False)
        gasto_admin.save()
        return super(AdminCostCreateView, self).form_valid(form)
    
class AdminCostUpdateView(UpdateView):
    model = GastoAdministrativo
    template_name = "inputapp/update_admin.html"
    fields = '__all__'
    success_url = reverse_lazy('inputapp:correcto')
    
    def post(self, request, *args, **kwargs):
        self.object  = self.get_object()
        print("*******METODO POST*******")
        print("=========================")
        return super().post(request, *args, **kwargs)
      
    def form_valid(self, form):
        #logica del proceso
        print("*******VALIDACION********")
        print("*************************")
        return super(AdminCostUpdateView, self).form_valid(form)
   
class AdminCostDeleteView(DeleteView):
    model = GastoAdministrativo
    template_name = "inputapp/borrar_admin.html"
    success_url = reverse_lazy('inputapp:correcto')     
   


class ListElectricCost(ListView):
    template_name="pages/list_g_electro.html"
    model = GastoElectrico 
    paginate_by = 4
    ordering = "nombre"
    context_object_name ="Electric Cost"

class ElectricCostCreateView(CreateView):
    template_name = 'inputapp/create_g_electro.html'
    model = GastoElectrico
    fields = '__all__'
    success_url = reverse_lazy('inputapp:correcto')
    
    def form_valid(self, form):
            #logica del proceso
        electric_cost = form.save(commit=False)
        electric_cost.save()
        return super(ElectricCostCreateView, self).form_valid(form)
    
    
    
class ElectricCostUpdateView(UpdateView):
    model = GastoElectrico
    template_name = "inputapp/update_electric.html"
    fields = '__all__'
    success_url = reverse_lazy('inputapp:correcto')
    
    def post(self, request, *args, **kwargs):
        self.object  = self.get_object()
        print("*******METODO POST*******")
        print("=========================")
        return super().post(request, *args, **kwargs)
      
    def form_valid(self, form):
        #logica del proceso
        print("*******VALIDACION********")
        print("*************************")
        return super(ElectricCostUpdateView, self).form_valid(form)
   
class ElectricCostDeleteView(DeleteView):
    model = GastoElectrico
    template_name = "inputapp/borrar_electric.html"
    success_url = reverse_lazy('inputapp:correcto')   


class GasCostCreateView(CreateView):
    template_name = 'inputapp/create_g_gas.html'
    model = GastoGas
    fields = '__all__'
    success_url = 'reverse_lazy(inputapp:correcto)'
    
    def form_valid(self, form):
            #logica del proceso
        gasto_gas = form.save(commit=False)
        gasto_gas.save()
        return super(GasCostCreateView, self).form_valid(form)
    
    
    
class GasCostUpdateView(UpdateView):
    model = GastoGas
    template_name = "inputapp/update_gas.html"
    fields = '__all__'
    success_url = reverse_lazy('inputapp:correcto')
    
    def post(self, request, *args, **kwargs):
        self.object  = self.get_object()
        print("*******METODO POST*******")
        print("=========================")
        return super().post(request, *args, **kwargs)
      
    def form_valid(self, form):
        #logica del proceso
        print("*******VALIDACION********")
        print("*************************")
        return super(GasCostUpdateView, self).form_valid(form)
   
class GasCostDeleteView(DeleteView):
    model = GastoGas
    template_name = "inputapp/borrar_gascost.html"
    success_url = reverse_lazy('inputapp:correcto')   



class FertilizerCostCreateView(CreateView):
    template_name = 'inputapp/create_g_fertilizante.html'
    model = GastoFertilizante
    fields = '__all__'
    success_url = 'reverse_lazy(inputapp:correcto)'
    
    def form_valid(self, form):
            #logica del proceso
        gasto_fertilizante = form.save(commit=False)
        gasto_fertilizante.save()
        return super(FertilizerCostCreateView, self).form_valid(form)
    


class FertilizerCostUpdateView(UpdateView):
    model = GastoFertilizante
    template_name = "inputapp/update_fertilizer.html"
    fields = '__all__'
    success_url = reverse_lazy('inputapp:correcto')
    
    def post(self, request, *args, **kwargs):
        self.object  = self.get_object()
        print("*******METODO POST*******")
        print("=========================")
        return super().post(request, *args, **kwargs)
      
    def form_valid(self, form):
        #logica del proceso
        print("*******VALIDACION********")
        print("*************************")
        return super(FertilizerCostUpdateView, self).form_valid(form)
   
class FertilizerCostDeleteView(DeleteView):
    model = GastoFertilizante
    template_name = "inputapp/borrar_fertilizer.html"
    success_url = reverse_lazy('inputapp:correcto') 






class SubstrateCostCreateView(CreateView):
    template_name = 'inputapp/create_g_substrato.html'
    model = GastoSubstrato
    fields = '__all__'
    success_url = 'reverse_lazy(inputapp:correcto)'

    def form_valid(self, form):
            #logica del proceso
        gasto_substrato = form.save(commit=False)
        gasto_substrato.save()
        return super(SubstrateCostCreateView, self).form_valid(form)

    
class SubstrateCostUpdateView(UpdateView):
    model = GastoSubstrato
    template_name = "inputapp/update_substrate.html"
    fields = '__all__'
    success_url = reverse_lazy('inputapp:correcto')
    
    def post(self, request, *args, **kwargs):
        self.object  = self.get_object()
        print("*******METODO POST*******")
        print("=========================")
        return super().post(request, *args, **kwargs)
      
    def form_valid(self, form):
        #logica del proceso
        print("*******VALIDACION********")
        print("*************************")
        return super(SubstrateCostUpdateView, self).form_valid(form)
   
class SubstrateCostDeleteView(DeleteView):
    model = GastoSubstrato
    template_name = "inputapp/borrar_substrate.html"
    success_url = reverse_lazy('inputapp:correcto')    




class ShippingCostCreateView(CreateView):
    template_name = 'inputapp/create_g_envio.html'
    model = GastoEnvio
    fields = '__all__'
    success_url = 'reverse_lazy(inputapp:correcto)'
    
    def form_valid(self, form):
            #logica del proceso
        gasto_shipping = form.save(commit=False)
        gasto_shipping.save()
        return super(ShippingCostCreateView, self).form_valid(form)
    
    
class ShippingCostUpdateView(UpdateView):
    model = GastoEnvio
    template_name = "inputapp/update_shipping.html"
    ffields = '__all__'
    success_url = reverse_lazy('inputapp:correcto')
    
    def post(self, request, *args, **kwargs):
        self.object  = self.get_object()
        print("*******METODO POST*******")
        print("=========================")
        return super().post(request, *args, **kwargs)
      
    def form_valid(self, form):
        #logica del proceso
        print("*******VALIDACION********")
        print("*************************")
        return super(ShippingCostUpdateView, self).form_valid(form)
   
class ShippingCostDeleteView(DeleteView):
    model = GastoEnvio
    template_name = "inputapp/borrar_shipping.html"
    success_url = reverse_lazy('inputapp:correcto')  




class SeedsCostCreateView(CreateView):
    template_name = 'inputapp/create_g_semillas.html'
    model = GastoSemillas
    fields = '__all__'
    success_url = 'reverse_lazy(inputapp:correcto)'
    
    def form_valid(self, form):
            #logica del proceso
        gasto_seeds = form.save(commit=False)
        gasto_seeds.save()
        return super(SeedsCostCreateView, self).form_valid(form)
    
    
class SeedsCostUpdateView(UpdateView):
    model = GastoSemillas
    template_name = "inputapp/update_seeds.html"
    fields = '__all__'
    success_url = reverse_lazy('inputapp:correcto')
    
    def post(self, request, *args, **kwargs):
        self.object  = self.get_object()
        print("*******METODO POST*******")
        print("=========================")
        return super().post(request, *args, **kwargs)
      
    def form_valid(self, form):
        #logica del proceso
        print("*******VALIDACION********")
        print("*************************")
        return super(SeedsCostUpdateView, self).form_valid(form)


class SeedsCostDeleteView(DeleteView):
    model = GastoSemillas
    template_name = "inputapp/borrar_seeds.html"
    success_url = reverse_lazy('inputapp:correcto')  




class FuelCostCreateView(CreateView):
    template_name = 'inputapp/create_g_combustible.html'
    model = GastoCombustible
    fields = '__all__'
    success_url = 'reverse_lazy(inputapp:correcto)'
    
    def form_valid(self, form):
            #logica del proceso
        gasto_fuel = form.save(commit=False)
        gasto_fuel.save()
        return super(FuelCostCreateView, self).form_valid(form)
    
    
class FuelCostUpdateView(UpdateView):
    model = GastoCombustible
    template_name = "inputapp/update_fuel.html"
    fields = '__all__'
    success_url = reverse_lazy('inputapp:correcto')
    
    def post(self, request, *args, **kwargs):
        self.object  = self.get_object()
        print("*******METODO POST*******")
        print("=========================")
        
        return super().post(request, *args, **kwargs)
      
    def form_valid(self, form):
        #logica del proceso
        print("*******VALIDACION********")
        print("*************************")
        return super(FuelCostUpdateView, self).form_valid(form)
   
class FuelCostDeleteView(DeleteView):
    model = GastoCombustible
    template_name = "inputapp/borrar_fuel.html"
    success_url = reverse_lazy('inputapp:correcto')  




class CleaningCostCreateView(CreateView):
    template_name = 'inputapp/create_g_limpieza.html'
    model = GastoLimpieza
    fields = '__all__'
    success_url = 'reverse_lazy(inputapp:correcto)'
    
    def form_valid(self, form):
            #logica del proceso
        gasto_cleaning = form.save(commit=False)
        gasto_cleaning.save()
        return super(CleaningCostCreateView, self).form_valid(form)
    
    
class CleaningCostUpdateView(UpdateView):
    model = GastoLimpieza
    template_name = "inputapp/update_cleaning.html"
    fields = '__all__'
    success_url = reverse_lazy('inputapp:correcto')
    
    def post(self, request, *args, **kwargs):
        self.object  = self.get_object()
        print("*******METODO POST*******")
        print("=========================")
        return super().post(request, *args, **kwargs)
      
    def form_valid(self, form):
        #logica del proceso
        print("*******VALIDACION********")
        print("*************************")
        return super(CleaningCostUpdateView, self).form_valid(form)
   
class CleaningCostDeleteView(DeleteView):
    model = GastoLimpieza
    template_name = "inputapp/borrar_cleaning.html"
    success_url = reverse_lazy('inputapp:correcto')  

class RemediesCostCreateView(CreateView):
    template_name = 'inputapp/create_g_remedio.html'
    model = GastoRemedio
    fields = '__all__'
    success_url = 'reverse_lazy(inputapp:correcto)'
    
    def form_valid(self, form):
            #logica del proceso
        gasto_various = form.save(commit=False)
        gasto_various.save()
        return super(VariousCostCreateView, self).form_valid(form)
    
    
class RemediesCostUpdateView(UpdateView):
    model = GastoRemedio
    template_name = "inputapp/update_remedio.html"
    fields = '__all__'
    success_url = reverse_lazy('inputapp:correcto')
    
    def post(self, request, *args, **kwargs):
        self.object  = self.get_object()
        print("*******METODO POST*******")
        print("=========================")
        return super().post(request, *args, **kwargs)
      
    def form_valid(self, form):
        #logica del proceso
        print("*******VALIDACION********")
        print("*************************")
        return super(VariousCostUpdateView, self).form_valid(form)
   
class RemediesCostDeleteView(DeleteView):
    model = GastoRemedio
    template_name = "inputapp/borrar_remedio.html"
    success_url = reverse_lazy('inputapp:correcto')



class VariousCostCreateView(CreateView):
    template_name = 'inputapp/create_g_vario.html'
    model = VariosGasto
    fields = '__all__'
    success_url = 'reverse_lazy(inputapp:correcto)'
    
    def form_valid(self, form):
            #logica del proceso
        gasto_various = form.save(commit=False)
        gasto_various.save()
        return super(VariousCostCreateView, self).form_valid(form)
    
    
class VariousCostUpdateView(UpdateView):
    model = VariosGasto
    template_name = "inputapp/update_various.html"
    fields = '__all__'
    success_url = reverse_lazy('inputapp:correcto')
    
    def post(self, request, *args, **kwargs):
        self.object  = self.get_object()
        print("*******METODO POST*******")
        print("=========================")
        return super().post(request, *args, **kwargs)
      
    def form_valid(self, form):
        #logica del proceso
        print("*******VALIDACION********")
        print("*************************")
        return super(VariousCostUpdateView, self).form_valid(form)
   
class VariousCostDeleteView(DeleteView):
    model = VariosGasto
    template_name = "inputapp/borrar_various.html"
    success_url = reverse_lazy('inputapp:correcto')  




class MacroeconomicsIndicatorsCreateView(CreateView):
    template_name = 'inputapp/create_g_macroeconomics.html'
    model = macroeconomicsIndicators
    fields = '__all__'
    success_url = 'reverse_lazy(inputapp:correcto)'
    
    def form_valid(self, form):
            #logica del proceso
        gasto_various = form.save(commit=False)
        gasto_various.save()
        return super(VariousCostCreateView, self).form_valid(form)
    
    
class MacroeconomicsIndicatorsUpdateView(UpdateView):
    model = macroeconomicsIndicators
    template_name = "inputapp/update_g_macroeconomics.html"
    fields = '__all__'
    success_url = reverse_lazy('inputapp:correcto')
    
    def post(self, request, *args, **kwargs):
        self.object  = self.get_object()
        print("*******METODO POST*******")
        print("=========================")
        return super().post(request, *args, **kwargs)
      
    def form_valid(self, form):
        #logica del proceso
        print("*******VALIDACION********")
        print("*************************")
        return super(VariousCostUpdateView, self).form_valid(form)
   
class MacroeconomicsIndicatorsDeleteView(DeleteView):
    model = macroeconomicsIndicators
    template_name = "inputapp/borrar_macroeconomics.html"
    success_url = reverse_lazy('inputapp:correcto')  
    

class taxRateCreateView(CreateView):
    template_name = 'inputapp/create_g_taxrate.html'
    model = taxRate
    fields = '__all__'
    success_url = 'reverse_lazy(inputapp:correcto)'
    
    def form_valid(self, form):
            #logica del proceso
        gasto_various = form.save(commit=False)
        gasto_various.save()
        return super(VariousCostCreateView, self).form_valid(form)
    
    
class taxRateUpdateView(UpdateView):
    model = taxRate
    template_name = "inputapp/update_taxrate.html"
    model = taxRate
    fields = '__all__'
    success_url = reverse_lazy('inputapp:correcto')
    
    def post(self, request, *args, **kwargs):
        self.object  = self.get_object()
        print("*******METODO POST*******")
        print("=========================")
        return super().post(request, *args, **kwargs)
      
    def form_valid(self, form):
        #logica del proceso
        print("*******VALIDACION********")
        print("*************************")
        return super(VariousCostUpdateView, self).form_valid(form)
   
class taxRateDeleteView(DeleteView):
    model = taxRate
    template_name = "inputapp/borrar_taxrate.html"
    success_url = reverse_lazy('inputapp:correcto') 


class SuccesView(TemplateView):
    template_name = "inputapp/success.html"






# def proyecto_detail(request, id):
    
#     proyecto_detail = get_object_or_404(Proyecto, id=id)
#     return render(request,'inputapp/create_proyecto_detail.html',{
#         'title':'Proyecto',
#         'proyecto_detail':proyecto_detail
        
#     })
# def personal_detail(request,personal_id):
    
#     personal_detail = get_object_or_404(Personal, id=personal_id)
#     return render(request,'inputapp/g_personal.html',{
#         'title':'Gastos de personal'
#     })

# def admin_detail(request,GastoAdministrativo_id):
#     admin_detail = get_object_or_404(GastoAdministrativo, id=GastoAdministrativo_id)
#     return render(request,'inputapp/g_admin.html',{
#         'title':'Gastos administrativos',
#         'admin_detail':admin_detail
        
#     })
# def electro_detail(request,  GastoElectrico_id):
#     electro_detail = get_object_or_404(GastoElectrico, id= GastoElectrico_id)
#     return render(request,'inputapp/g_electro.html',{
#         'title':'Gastos de electricidad'
#     })
# def gas_detail(request,GastoGas_id):
#     gas_detail = get_object_or_404(GastoGas, id= GastoGas_id)
#     return render(request,'inputapp/g_gas.html',{
#         'title':'Gastos de gas'
#     })
# def fertilizante_detail(request,GastoFertilizante_id):
#     gas_detail = get_object_or_404(GastoFertilizante, id= GastoFertilizante_id)
#     return render(request,'inputapp/g_fertilizante.html',{
#         'title':'Gastos de fertilizante'
#     })
# def substrato_detail(request,GastoSubstrato_id):
#     gas_detail = get_object_or_404(GastoSubstrato, id= GastoSubstrato_id)
#     return render(request,'inputapp/g_substrato.html',{
#         'title':'Gastos de substrato'
#     })
# def envio_detail(request,GastoEnvio_id):
#     gas_detail = get_object_or_404(GastoEnvio, id= GastoEnvio_id)
#     return render(request,'inputapp/g_envio.html',{
#         'title':'Gastos de envíos'
#     })
# def remedio_detail(request,GastoRemedio_id):
#     gas_detail = get_object_or_404(GastoRemedio, id= GastoRemedio_id) 
#     return render(request,'inputapp/g_remedio.html',{
#         'title': 'Gastos de remedios'
#     })
# def semillas_detail(request,GastoSemillas_id):
#     gas_detail = get_object_or_404(GastoSemillas, id= GastoSemillas_id) 
#     return render(request,'inputapp/g_semillas.html',{
#         'title':'Gastos de semillas'
#     })
# def combustible_detail(request,GastoCombustible_id):
#     gas_detail = get_object_or_404(GastoCombustible, id= GastoCombustible_id) 
#     return render(request,'inputapp/g_combustible.html',{
#         'title':'Gastos de combustible'
#     })
# def limpieza_detail(request,GastoLimpieza_id):
#     gas_detail = get_object_or_404(GastoLimpieza, id= GastoLimpieza_id)
#     return render(request,'inputapp/g_limpieza.html',{
#         'title':'Gastos de limpieza'        
#     })
# def gastovario_detail(request,VariosGasto_id):
#     gastovario_detail = get_object_or_404(VariosGasto ,id= VariosGasto_id)
#     return render(request,'inputapp/g_vario.html',{
        
#     })
    
# def crear_proyecto(request, nombre, description, fecha_inicio, fecha_final, created_at, updated_at, user,slug):
#     proyecto = Proyecto(
#         nombre =nombre,
#         description= description,
#         fecha_inicio = fecha_inicio,
#         fecha_final = fecha_final,
#         created_at = created_at,
#         updated_at = updated_at,
#         user = user,
#         slug = slug,    
#     )
    
#     proyecto.save()
         
#     return HttpResponse("Usuario creado: ") 


# def proyecto(request):
    
#     try:
#         proyecto = Proyecto.objects.get(user = 'javi')
#         response = f"Proyecto: <br/> {proyecto.id}.{proyecto.nombre} "
#     except:
#         response ="<h2>Proyecto no encontrado </h2>"
#     return HttpResponse(response)

# def editar_proyecto(request, id):
#     proyecto =Proyecto.objects.get(pk=id)
#     proyecto.nombre = "Proyecto 1 bis"
        
#     proyecto.save()

#     return HttpResponse(f"Proyecto editado :  {proyecto.nombre}")

# def save_proyecto(request):
    
#     if request.method == "POST":
        
#         nombre = request.POST['nombre']
        
#         if len(title) <= 5:
#             return HttpResponse("El título es demasiado pequeño")
        
#         description = request.POST['description']
#         fecha_inicio = request.POST['fecha_inicio']
#         fecha_final = request.POST['fecha_final']
        
#     proyecto = Proyecto(
#         nombre =nombre,
#         description= description,
#         fecha_inicio = fecha_inicio,
#         fecha_final = fecha_final,
       
#     )
    
#     proyecto.save()
         
#     return HttpResponse("Usuario creado: ")     

# def create_proyecto(request):
#     return render(request,'inputapp/create_proyecto.html',{
#         'title':'Crear proyecto',
#         })

# def create_full_proyecto(request):
    
#     formulario = FormProyecto()
    
#     return render(request, 'create_full_proyecto.html',{
#         'form':formulario
#     })

# def proyectos(request):
    
#     proyectos = Proyecto.objects.all()
    
#     return render(request, 'inputapp/list_proyectos.html',{
#         'proyectos' : proyectos
#     })