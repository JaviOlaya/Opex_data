from django.contrib import admin

from .models import (
    Proyecto,
    Personal,
    GastoAdministrativo,
    GastoElectrico,
    GastoGas,
    GastoFertilizante,
    GastoSubstrato,
    GastoEnvio,
    GastoRemedio,
    GastoSemillas,
    GastoCombustible,
    GastoLimpieza,
    VariosGasto,
    taxRate,
    macroeconomicsIndicators
    )
# Register your models here.

class ProyectoAdmin(admin.ModelAdmin):
    list_display=[
        'id',
        'nombre',
        'area_total',
        'created_at',
        'user',
    ]
    readonly_fields=('created_at','updated_at','user')
    def save_model(self, request, obj, form, change):
        if not obj.user_id:
            obj.user_id = request.user.id
        obj.save()


class PersonalAdmin(admin.ModelAdmin):
    readonly_fields=('created_at','updated_at',)
    def save_model(self, request, obj, form, change):
        if not obj.proyecto_id:
            obj.proyecto_id = request.proyecto.nombre
        obj.save()

class GastoAdministrativoAdmin(admin.ModelAdmin):
    readonly_fields=('created_at','updated_at',)
    def save_model(self, request, obj, form, change):
        if not obj.proyecto_id:
            obj.proyecto_id = request.proyecto.nombre
        obj.save()     
        
class GastoElectricoAdmin(admin.ModelAdmin):
    readonly_fields=('created_at','updated_at',)
    def save_model(self, request, obj, form, change):
        if not obj.proyecto_id:
            obj.proyecto_id = request.proyecto.nombre
        obj.save()     

class GastoGasAdmin(admin.ModelAdmin):
    readonly_fields=('created_at','updated_at',)
    def save_model(self, request, obj, form, change):
        if not obj.proyecto_id:
            obj.proyecto_id = request.proyecto.nombre
        obj.save()   

class GastoFertilizanteAdmin(admin.ModelAdmin):
    readonly_fields=('created_at','updated_at',)
    def save_model(self, request, obj, form, change):
        if not obj.proyecto_id:
            obj.proyecto_id = request.proyecto.nombre
        obj.save()   



class GastoSubstratoAdmin(admin.ModelAdmin):
    readonly_fields=('created_at','updated_at',)
    def save_model(self, request, obj, form, change):
        if not obj.proyecto_id:
            obj.proyecto_id = request.proyecto.nombre
        obj.save()   

class GastoEnvioAdmin(admin.ModelAdmin):
    readonly_fields=('created_at','updated_at',)
    def save_model(self, request, obj, form, change):
        if not obj.proyecto_id:
            obj.proyecto_id = request.proyecto.nombre
        obj.save()  


class GastoRemedioAdmin(admin.ModelAdmin):
    readonly_fields=('created_at','updated_at',)
    def save_model(self, request, obj, form, change):
        if not obj.proyecto_id:
            obj.proyecto_id = request.proyecto.nombre
        obj.save()  


class GastoSemillasAdmin(admin.ModelAdmin):
    readonly_fields=('created_at','updated_at',)
    def save_model(self, request, obj, form, change):
        if not obj.proyecto_id:
            obj.proyecto_id = request.proyecto.nombre
        obj.save()  


class GastoCombustibleAdmin(admin.ModelAdmin):
    readonly_fields=('created_at','updated_at',)
    def save_model(self, request, obj, form, change):
        if not obj.proyecto_id:
            obj.proyecto_id = request.proyecto.nombre
        obj.save()  


class GastoLimpiezaAdmin(admin.ModelAdmin):
    readonly_fields=('created_at','updated_at',)
    def save_model(self, request, obj, form, change):
        if not obj.proyecto_id:
            obj.proyecto_id = request.proyecto.nombre
        obj.save()  


class taxRateAdmin(admin.ModelAdmin):
    # readonly_fields=('created_at','updated_at',)
    def save_model(self, request, obj, form, change):
        if not obj.proyecto_id:
            obj.proyecto_id = request.proyecto.nombre
        obj.save()  

class VariosGastoAdmin(admin.ModelAdmin):
    readonly_fields=('created_at','updated_at',)
    def save_model(self, request, obj, form, change):
        if not obj.proyecto_id:
            obj.proyecto_id = request.proyecto.nombre
        obj.save()  


class macroeconomicsIndicatorsAdmin(admin.ModelAdmin):
    readonly_fields=('created_at','updated_at',)
    def save_model(self, request, obj, form, change):
        if not obj.proyecto_id:
            obj.proyecto_id = request.proyecto.nombre
        obj.save()  


admin.site.register(Proyecto,ProyectoAdmin)
admin.site.register(Personal,PersonalAdmin)
admin.site.register(GastoAdministrativo,GastoAdministrativoAdmin)
admin.site.register(GastoElectrico,GastoElectricoAdmin)
admin.site.register(GastoGas,GastoGasAdmin)
admin.site.register(GastoFertilizante,GastoFertilizanteAdmin)
admin.site.register(GastoSubstrato,GastoSubstratoAdmin)
admin.site.register(GastoEnvio,GastoEnvioAdmin)
admin.site.register(GastoRemedio,GastoRemedioAdmin)
admin.site.register(GastoSemillas,GastoSemillasAdmin)
admin.site.register(GastoCombustible,GastoCombustibleAdmin)
admin.site.register(GastoLimpieza,GastoLimpiezaAdmin)
admin.site.register(VariosGasto,VariosGastoAdmin)
admin.site.register(taxRate,taxRateAdmin)
admin.site.register(macroeconomicsIndicators,macroeconomicsIndicatorsAdmin)