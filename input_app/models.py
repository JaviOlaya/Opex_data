from django.db import models
from django.conf import settings
# Create your models here.

class GastosCultivo(models.Model):
    title = models.CharField(max_length=150, verbose_name="Título")
    content = models.CharField(max_length=300, verbose_name="Descripción")
    potencia_electrica = models.FloatField(default=0, verbose_name="Potencia eléctrica")
    gas= models.FloatField(default=0, verbose_name="Gas")
    fertilizante = models.FloatField(default=0, verbose_name="Fertilizante")
    substrato = models.FloatField(default=0, verbose_name="Substrato")
    empacado_y_transporte =  models.FloatField(default=0, verbose_name="Empacado_y_transporte")
    remedios = models.FloatField(default=0, verbose_name="Remedios")
    semillas = models.FloatField(default=0, verbose_name="Semillas")
    material_cultivo = models.FloatField(default=0, verbose_name="Material_cultivo")
    insectos = models.FloatField(default=0, verbose_name="Insectos")
    
    
class GastosGenerales(models.Model):
    
    personal = models.PositiveIntegerField('Stock', default=0)
    sueldos_con_contribucion = models.FloatField(default=0, verbose_name="sueldo")
    consulta_agricola = models.FloatField(default=0, verbose_name="Consultoría agrícola")
    formacion = models.FloatField(default=0, verbose_name="Formación")
    POL_gastos_admin = models.FloatField(default=0, verbose_name="POL gastos administrativos")
    gastos_oficina = models.FloatField(default=0, verbose_name="Gastos de oficina")
    gastos_viajes = models.FloatField(default=0, verbose_name="Gastos de Viajes")
    gastos_mantenimiento = models.FloatField(default=0, verbose_name="Gastos mantenimiento") 
    gastos_servicios_informacion = models.FloatField(default=0, verbose_name="Gastos servicios de información") 
    gastos_seguro_propiedad = models.FloatField(default=0, verbose_name="Seguo de la propiedad") 



        