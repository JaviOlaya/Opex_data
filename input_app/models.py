from django.db import models 
from django.db.models import Model 
from django.conf import settings
# Create your models here.
# Create your models here.
class Proyecto(models.Model):
    Nombre_proyecto  = models.CharField(max_length=50)
    Fecha_de_inicio = models.DateField()

    def DatosProyecto(self):
        cadena = "Nombre:{0}"
        return cadena.format(self.Nombre_proyecto,self.Fecha_de_inicio)
    
    def __str__ (self):
        return self.DatosProyecto()
        
        
class Personal(models.Model):
    DEPARTAMENTO_CHOICES = (
        ('0', 'Gerente'),
        ('1', 'Comercial'),
        ('2', 'Administrativo'),
        ('3', 'Soporte')
    )
    # PrimerApellido = models.CharField(max_length=50)
    # SegundoApellido = models.CharField(max_length=50)
    # Nombres= models.CharField(max_length=50)
    # DNI = models.CharField(max_length=8)
    FondoFijo = models.BooleanField(default='true')
    # FechaNacimiento = models.DateField()
    # Sexos=(('F','Femenino'),('M','Masculino'))
    # Sexo = models.CharField(max_length=1, choices=Sexos,default='M')
    Num_empleados =models.PositiveIntegerField(default='0')
    Plantillas = models.CharField(
        'Departamento',
        max_length=30,
        choices= DEPARTAMENTO_CHOICES,
        default='0', 
    )
  
    Sueldo = models.FloatField(default='0')
    
    def DatosPersonal(self):
        cadena ="Datos de empleados:{0}"
        # return cadena.format(self.PrimerApellido,self.SegundoApellido,self.Nombres)
        return cadena.format(self.Plantillas,self.Num_empleados)
   
    def __str__ (self):
        return self.DatosPersonal()


class GastosAdministrativos(models.Model):
    GADMIN_CHOICES = (
        ('0', 'Consulta Agricola'),
        ('1', 'Formación'),
        ('2', 'Entrenamiento'),
        ('3', 'POL en necesidades administrativas'),
        ('4', 'Gastos de Oficina'),
        ('5', 'Gastos de Entretenimiento'),
        ('6', 'Gastos de Viajes'),
        ('7', 'Servicios de Información'),
        ('8', 'Gasto seguro de propiedad'),
        
    )
    Nombre =models.CharField(max_length=50)
    Descripcion = models.TextField(max_length=200,blank=True)
    FechaGasto=models.DateField()
    Cantidad= models.FloatField(default='0')
   
    TipoGasto = models.CharField(max_length=1,choices=GADMIN_CHOICES,default='0')
    
    def DatosGastosAdministrativos(self):
        cadena = "{0},{1}"
        return cadena.format(self.Nombre, self.TipoGasto)    
    
    def __str__(self):
        return self.DatosGastosAdministrativos()

class GastosCultivos(models.Model):

    UNIT_CHOICES = (
        ('0', 'Kilogramos'),
        ('1', 'Litros'),
        ('2', 'Unidades'),
    )

    FechaActualizacion= models.DateField()
    PotElectricaPrecio=models.DecimalField(max_digits=7, decimal_places=2)
    CantidadPotElec=models.DecimalField(max_digits=7, decimal_places=2)
    unitPotElec = models.CharField(
        'unidad de medida',
        max_length=30,
        choices=UNIT_CHOICES, 
        default='Kilogramos',
    )
    PrecioGas= models.DecimalField(max_digits=7, decimal_places=2)
    CantidadGas=models.DecimalField(max_digits=7, decimal_places=2)
    unitGas = models.CharField(
        'unidad de medida',
        max_length=30,
        choices=UNIT_CHOICES,
        default='Kilogramos',
    )
    FertilizantePrecio = models.DecimalField(max_digits=7, decimal_places=2)
    CantidadFertilizante=models.DecimalField(max_digits=7, decimal_places=2)
    unitFertilizante = models.CharField(
        'unidad de medida',
        max_length=30,
        choices=UNIT_CHOICES,
        default='Kilogramos',
    )
    SubstratoPrecio = models.DecimalField(max_digits=7, decimal_places=2)
    CantidadSubstrato = models.DecimalField(max_digits=7, decimal_places=2)
    unitSubstrato = models.CharField(
        'unidad de medida',
        max_length=30,
        choices=UNIT_CHOICES,
        default='Kilogramos',
    )
    Empaquetamiento_TransportePrecio=models.DecimalField(max_digits=7, decimal_places=2)
    
    RemediosPrecio=models.DecimalField(max_digits=7, decimal_places=2)
    CantidadRemedios=models.DecimalField(max_digits=7, decimal_places=2)
    unitRemedios = models.CharField(
        'unidad de medida',
        max_length=30,
        choices=UNIT_CHOICES,
        default='Kilogramos',
    )
    SemillasPrecio = models.DecimalField(max_digits=7, decimal_places=2)
    CantidadSemillas = models.DecimalField(max_digits=7, decimal_places=2)
    unitSemillas = models.CharField(
        'unidad de medida',
        max_length=30,
        choices=UNIT_CHOICES,
        default='Kilogramos', 
    )
    
    CombustiblePrecio = models.DecimalField(max_digits=7, decimal_places=2)
    CantidadCombustible = models.DecimalField(max_digits=7, decimal_places=2)
    unitCombustible = models.CharField(
        'unidad de medida',
        max_length=30,
        choices=UNIT_CHOICES,
        default='Kilogramos', 
    )
    
    EquipoCultivoPrecio = models.DecimalField(max_digits=7, decimal_places=2)
   
    RetiradaBasuraSolidaPrecio = models.DecimalField(max_digits=7, decimal_places=2)
    OtrosGastos = models.DecimalField(max_digits=7, decimal_places=2)
    RopaDeTrabajoGastos = models.DecimalField(max_digits=7, decimal_places=2)
    CertificacionGastos = models.DecimalField(max_digits=7, decimal_places=2)
    GastosLimpiezaAguasResiduales= models.DecimalField(max_digits=7, decimal_places=2)
    CantidadLimpiezaAguasResiduales= models.DecimalField(max_digits=7, decimal_places=2)
    unitLimpiezaAguasResiduales = models.CharField(
        'unidad de medida',
        max_length=30,
        choices=UNIT_CHOICES,
        default='Kilogramos',
    )
    
    def GastosCultivosTotal(self):
        cadena = "Fecha actualización: {0}"
        return cadena.format(self.FechaActualizacion)

    def __str__ (self):
        return self.GastosCultivosTotal()
    
# class CapitalTrabajo(models.Model):
    

