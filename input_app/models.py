from django.db import models 
from django.db.models import Model 
from django.conf import settings
# Create your models here.

# Create your models here.
class Personal(models.Model):
    FondoFijo = models.BooleanField(default='true')
    Num_empleados =models.PositiveIntegerField(default='0')
    Plantillas = (('Gerente','Gerente'), ('Comercial','Comercial'),('Administrativo','Administrativo'),('Soporte','Soporte'))
    Plantilla = models.CharField(max_length=20,choices=Plantillas,default='S')
    Sueldo = models.FloatField(default='0')
    
    def DatosPersonal(self):
        cadena ="Datos de empleados:{0}"
        # return cadena.format(self.PrimerApellido,self.SegundoApellido,self.Nombres)
        return cadena.format(self.Plantilla,self.Num_empleados)
   
    def __str__ (self):
        return self.DatosPersonal()


class GastosAdministrativos(models.Model):
    Nombre =models.CharField(max_length=50)
    Descripcion = models.TextField(max_length=200,blank=True)
    FechaGasto=models.DateField()
    Cantidad= models.FloatField(default='0')
    Tipo = (('Consulta Agricola','Agronomy_consulting'),('Formación','Formacion'),('Entrenamiento','Entrenamiento'),('Necesidades administrativas','POL on administrative needs'),('Gastos de Oficina','Office_expenses'),('Gastos de Entretenimiento','Entertainment_expenses'),('Gastos de Viajes','Travel_expenses'),('Servicios de Información','Information_services'),('Gasto seguro de propiedad','Property_Insurance'))
    TipoGasto = models.CharField(max_length=30,choices=Tipo,default='Consulta Agricola')
    
    def DatosGastosAdministrativos(self):
        cadena = "{0},{1}"
        return cadena.format(self.Nombre, self.TipoGasto)    
    
    def __str__(self):
        return self.DatosGastosAdministrativos()

class GastosCultivos(models.Model):
    UNIT_CHOICES = (
        ('Kilogramos', 'Kilogramos'),
        ('Litros', 'Litros'),
        ('Unidades', 'Unidades'),
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
    SemillasPrecio = models.DecimalField(max_digits = 7, decimal_places = 2)
    CantidadSemillas = models.DecimalField(max_digits = 7, decimal_places = 2)
    unitSemillas = models.CharField(
        'unidad de medida',
        max_length=30,
        choices=UNIT_CHOICES,
        default='Kilogramos', 
    )
    
    CombustiblePrecio = models.DecimalField(max_digits = 7, decimal_places = 2)
    CantidadCombustible = models.DecimalField(max_digits = 7 , decimal_places=2)
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
    
class CapitalTrabajo(models.Model):
    CapitalStock = models.DecimalField(max_digits=7, decimal_places=2)
    monedaStock = models.CharField(max_length=1,default='€')
    CapitalDeudores = models.DecimalField(max_digits=7, decimal_places=2)
    monedaDeudores = models.CharField(max_length=1,default='€')
    CapitalAcreedores = models.DecimalField(max_digits=7, decimal_places=2)
    monedaAcreedores = models.CharField(max_length=1,default='€')

    def CapitalTrabajoTotal(self):
        cadena = " {0}"
        return cadena.format(self.CapitalStock)

    def __str__ (self):
        return self.CapitalTrabajoTotal()
    
    