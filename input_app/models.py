from django.db import models
from django.conf import settings
# Create your models here.

# Create your models here.
class Personal(models.Model):
    # PrimerApellido = models.CharField(max_length=50)
    # SegundoApellido = models.CharField(max_length=50)
    # Nombres= models.CharField(max_length=50)
    # DNI = models.CharField(max_length=8)
    FondoFijo = models.BooleanField(default='true')
    # FechaNacimiento = models.DateField()
    # Sexos=(('F','Femenino'),('M','Masculino'))
    # Sexo = models.CharField(max_length=1, choices=Sexos,default='M')
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
    PotElectricaPrecio=models.FloatField(default="0")
    CantidadPotElec=models.FloatField(default="0")
    unitPotElec = models.CharField(
        'unidad de medida',
        max_length=30,
        choices=UNIT_CHOICES, 
        default='Kilogramos',
    )
    PrecioGas= models.FloatField(default="0")
    CantidadGas=models.FloatField(default="0")
    unitGas = models.CharField(
        'unidad de medida',
        max_length=30,
        choices=UNIT_CHOICES,
        default='Kilogramos',
    )
    FertilizantePrecio = models.FloatField(default="0")
    CantidadFertilizante=models.FloatField(default="0")
    unitFertilizante = models.CharField(
        'unidad de medida',
        max_length=30,
        choices=UNIT_CHOICES,
        default='Kilogramos',
    )
    SubstratoPrecio = models.FloatField(default="0")
    CantidadSubstrato = models.FloatField(default="0")
    unitSubstrato = models.CharField(
        'unidad de medida',
        max_length=30,
        choices=UNIT_CHOICES,
        default='Kilogramos',
    )
    Empaquetamiento_TransportePrecio=models.FloatField(default="0")
    
    RemediosPrecio=models.FloatField(default="0")
    CantidadRemedios=models.FloatField(default="0")
    unitRemedios = models.CharField(
        'unidad de medida',
        max_length=30,
        choices=UNIT_CHOICES,
        default='Kilogramos',
    )
    SemillasPrecio = models.FloatField(default="0")
    CantidadSemillas = models.FloatField(default="0")
    unitSemillas = models.CharField(
        'unidad de medida',
        max_length=30,
        choices=UNIT_CHOICES,
        default='Kilogramos', 
    )
    
    CombustiblePrecio = models.FloatField(default="0")
    CantidadCombustible = models.FloatField(default="0")
    unitCombustible = models.CharField(
        'unidad de medida',
        max_length=30,
        choices=UNIT_CHOICES,
        default='Kilogramos', 
    )
    
    EquipoCultivoPrecio = models.FloatField(default="0")
   
    RetiradaBasuraSolidaPrecio = models.FloatField(default="0")
    OtrosGastos = models.FloatField(default="0")
    RopaDeTrabajoGastos = models.FloatField(default="0")
    CertificacionGastos = models.FloatField(default="0")
    GastosLimpiezaAguasResiduales= models.FloatField(default="0")
    CantidadLimpiezaAguasResiduales= models.FloatField(default="0")
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
    stock

# class Rendicion(models.Model):
#     FechaIngresoSistema=models.DateField()
#     Nombre=models.CharField(max_length=30)
#     Monto=models.PositiveIntegerField(default='0')
#     Restriccion=models.CharField(max_length=30)
#     FechaEmisionDocumento=models.DateField(),
#     Tipo=(('C','Combustible'),('Co','Colación'),('P','Pasajes'),('R','Residencia'),('Pe','Peajes'),('S','Seleccionar'))
#     TipoGasto=models.CharField(max_length=2,choices=Tipo,default='S')
    
#     def NombreRinde(self):
#         cadena = "{0},{1},{2}"
#         return cadena.format(self.Nombre, self.Monto, self.TipoGasto)

#     def __str__ (self):
#         return self.NombreRinde()

# class Formacion(models.Model):
#   Personal= models.ForeignKey(Personal,null=False,blank=False,on_delete=models.CASCADE)
#   Rendicion=models.ForeignKey(Rendicion,null=False, blank=False,on_delete=models.CASCADE)
#   FechaRevision=models.DateTimeField(auto_now_add=True)
#   Restric=(('C','Colación no excede los 6500'),('Co','Combustible descuento 20%'),('R','Residencia justificada previo 3 cotizaciones'),('N','No hay'))
#   Restriccion=models.CharField(max_length=2,choices=Restric,default='N')
#   Estados=(('A','Aprobado'),('R','Rechazado'),('S','Seleccionar'))
  
#   def __str__(self):
#     cadena="{0}=>{1}"
#     return cadena.format(self.Personal,self.Rendicion.Nombre)

  
  
    
    