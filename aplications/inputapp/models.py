from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Proyecto(models.Model):
    id= models.AutoField(primary_key = True, verbose_name="ID")
    nombre= models.CharField(max_length=50, verbose_name="Nombre",default="Project default")
    description= models.TextField(max_length=300, blank=True,verbose_name="Descripción")
    fecha_inicio= models.DateTimeField(blank=True, verbose_name="Fecha de Inicio: ")
    fecha_final= models.DateTimeField(blank=True,null=True, verbose_name="Fecha finalización: ")
    created_at= models.DateTimeField(auto_now_add=True, verbose_name="Creado el:")
    updated_at= models.DateTimeField(auto_now=True, verbose_name="Actualizado el:")
    user= models.ForeignKey(User, blank=False, null=False, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name="Proyecto"
        verbose_name_plural="Proyectos"
    
    def DatosProyecto(self):
        cadena="Nombre del Proyecto:{0}"
        return cadena.format(self.nombre)

    def __str__ (self):
        return self.DatosProyecto()
    
class Personal(models.Model):
    DEPARTAMENTO_CHOICES = [
        ('0', 'Gerente'),
        ('1', 'Comercial'),
        ('2', 'Administrativo'),
        ('3', 'Soporte')
    ]
    numero_empleados = models.PositiveSmallIntegerField()
    plantilla =models.CharField(
        verbose_name="Departamento",
        max_length=20,
        choices=DEPARTAMENTO_CHOICES,default='0',
    )
    sueldo_empleado = models.DecimalField(max_digits=7, decimal_places=2,blank=True)
    proyecto= models.ForeignKey(Proyecto, verbose_name="Proyecto",blank=False,null=False, on_delete=models.CASCADE )
    created_at= models.DateTimeField(auto_now_add=True, verbose_name="Creado el:")
    updated_at= models.DateTimeField(auto_now=True, verbose_name="Actualizado el:")
    
        
    class Meta:
        verbose_name="Personal"
        verbose_name_plural ="Personal"
        
    def DatosPersonal(self):
        cadena = "Datos empleados Departamento: {0}, del proyecto: {1}"
        return cadena.format(self.plantilla, self.proyecto.nombre)
        
    def __str__ (self):
        return self.DatosPersonal()        

#Desde aquí empiezan los gastos

class GastoAdministrativo(models.Model):
    GADMIN_CHOICES = [
        ('0', 'Consulta Agricola'),
        ('1', 'Formación'),
        ('2', 'Entrenamiento'),
        ('3', 'POL en necesidades administrativas'),
        ('4', 'Gastos de Oficina'),
        ('5', 'Gastos de Entretenimiento'),
        ('6', 'Gastos de Viajes'),
        ('7', 'Servicios de Información'),
        ('8', 'Gasto seguro de propiedad'),
    ]
    Descripcion = models.TextField(max_length=200,blank=False)
    cantidadGasto = models.DecimalField(max_digits=7, decimal_places=2,blank=True, default='0')
    TipoGasto = models.CharField(max_length=1,choices=GADMIN_CHOICES,default='0')
    fecha_gasto = models.DateTimeField(blank=True,null=True,verbose_name="Gasto generado el:")  
    proyecto = models.ForeignKey(Proyecto, verbose_name="Proyecto",blank=False,null=False, on_delete=models.CASCADE )
    created_at= models.DateTimeField(auto_now_add=True, verbose_name="Creado el:")
    updated_at= models.DateTimeField(auto_now=True, verbose_name="Actualizado el:")
    
    def DatosGastoAdministrativo(self):
        cadena = "Gasto: {0}, fecha:{1}"
        return cadena.format(self.TipoGasto, self.fecha_gasto)
    
    class Meta:
        verbose_name: 'Gasto Administrativo'
        verbose_name_plural: 'Gastos Administrativos'
    
    def __str__ (self):
        return self.DatosGastoAdministrativo()

class GastoElectrico(models.Model):
    UNIT_CHOICES = [
        ('0', 'Kilogramos'),
        ('1', 'Litros'),
        ('2', 'Unidades'),
    ]
    fechaGasto = models.DateTimeField(blank=True,null=True,verbose_name="Gasto generado el:")
    
    CantidadPotElec = models.DecimalField(max_digits=7, decimal_places=2,blank=True)
    unitPotElec = models.CharField(
        'unidad de medida',
        max_length=1,
        choices=UNIT_CHOICES, 
        default='0',
    )
    PotElectricaPrecio = models.DecimalField(max_digits=7, decimal_places=2,blank=True)
    proyecto = models.ForeignKey(Proyecto, verbose_name="Proyecto",blank=False,null=False, on_delete=models.CASCADE)
    created_at =models.DateTimeField(auto_now_add=True, verbose_name="Creado el:")
    updated_at =models.DateTimeField(auto_now=True, verbose_name="Modificado el: ")
    
    def DatosGastoElectrico(self):
        cadena = "Fecha:{0}"
        return cadena.format(self.fechaGasto)
    
    class Meta:
        verbose_name: 'Gasto Eléctrico'
        verbose_name_plural: 'Gastos Eléctricos'
    
    def __str__ (self):
        return self.DatosGastoElectrico()

class GastoGas(models.Model):
    UNIT_CHOICES = [
        ('0', 'Kilogramos'),
        ('1', 'Litros'),
        ('2', 'Unidades'),
    ]      
    fechaGasto = models.DateTimeField(blank=True,null=True,verbose_name="Gasto generado el:")
    CantidadGas = models.DecimalField(max_digits=7, decimal_places=2,blank=True)
    unitGas = models.CharField(
        'unidad de medida',
        max_length=1,
        choices=UNIT_CHOICES, 
        default='0',
    )
    PrecioGas = models.DecimalField(max_digits=7, decimal_places=2,blank=True)
    proyecto = models.ForeignKey(Proyecto, verbose_name="Proyecto",blank=False,null=False, on_delete=models.CASCADE)
    created_at =models.DateTimeField(auto_now_add=True, verbose_name="Creado el:")
    updated_at =models.DateTimeField(auto_now=True, verbose_name="Modificado el: ")

    
    def DatosGastoGas(self):
        cadena = "Datos Consumo Gas: Consumo: {0},  Precio gas: {1} "
        return cadena.format(self.CantidadGas, self.PrecioGas)
    
    class Meta:
        verbose_name: 'Gasto de consumo de gas'
        verbose_name_plural: 'Gastos de consumo de gas'
    
    def __str__ (self):
        return self.DatosGastoGas()
    
class GastoFertilizante(models.Model):
    UNIT_CHOICES = [
        ('0', 'Kilogramos'),
        ('1', 'Litros'),
        ('2', 'Unidades'),    
    ]    
    fechaGasto = models.DateTimeField(blank=True,null=True,verbose_name="Gasto generado el:")
    CantidadFertilizante = models.DecimalField(max_digits=7,decimal_places=2,blank=True,)
    unitFertilizante = models.CharField(
        'unidad de medida',
        max_length=1,
        choices=UNIT_CHOICES, 
        default='0',
    )
    FertilizantePrecio = models.DecimalField(max_digits=7, decimal_places=2,blank=True,null=True)
    proyecto = models.ForeignKey(Proyecto, verbose_name="Proyecto",blank=False,null=False, on_delete=models.CASCADE )
    created_at= models.DateTimeField(auto_now_add=True,blank=True, verbose_name="Creado el:")
    updated_at= models.DateTimeField(auto_now=True,blank=True, verbose_name="Actualizado el:")

    def DatosGastoFertilizante(self):
        cadena = "Fecha gasto: {0} "
        return cadena.format(self.fechaGasto)
    
    class Meta:
        verbose_name: 'Gasto de consumo de fertilizante'
        verbose_name_plural: 'Gastos de consumo de fertilizantes'
    
    def __str__(self):
        return self.DatosGastoFertilizante()

class GastoSubstrato(models.Model):
    UNIT_CHOICES = [
        ('0', 'Kilogramos'),
        ('1', 'Litros'),
        ('2', 'Unidades'),
    ]
    fechaGasto = models.DateTimeField(blank=True,null=True,verbose_name="Gasto generado el:")
    SubstratoPrecio = models.DecimalField(max_digits=7, decimal_places=2,blank=True)
    CantidadSubstrato = models.DecimalField(max_digits=7, decimal_places=2,blank=True)
    unitSubstrato = models.CharField(
        'unidad de medida',
        max_length=1,
        choices=UNIT_CHOICES, 
        default='0',
    )
    proyecto = models.ForeignKey(Proyecto, verbose_name="Proyecto",blank=False,null=False, on_delete=models.CASCADE )
    created_at= models.DateTimeField(auto_now_add=True,blank=True, verbose_name="Creado el:")
    updated_at= models.DateTimeField(auto_now=True,blank=True, verbose_name="Actualizado el:")
    
    def DatosGastoSubstrato(self):
        cadena = "Datos Consumo fertilizante: Consumo: {0},  Precio fertilizante: {1} "
        return cadena.format(self.CantidadSubstrato, self.SubstratoPrecio)
    
    class Meta:
        verbose_name: 'Gasto de consumo de substrato'
        verbose_name_plural: 'Gastos de consumo de substratos'
    
    def __str__ (self):
        return self.DatosGastoSubstrato()
    
class GastoEnvio(models.Model):
  
    fechaGasto = models.DateTimeField(blank=True,null=True,verbose_name="Gasto generado el:")
    descripcion = models.TextField(max_length=200,blank=True) 
    EnvioPrecio = models.DecimalField(max_digits=7, decimal_places=2,blank=False)
    proyecto = models.ForeignKey(Proyecto, verbose_name="Proyecto",blank=False,null=False, on_delete=models.CASCADE )
    created_at= models.DateTimeField(auto_now_add=True,blank=True, verbose_name="Creado el:")
    updated_at= models.DateTimeField(auto_now=True,blank=True, verbose_name="Actualizado el:")
    
    def DatosGastoEnvio(self):
        cadena = "Fecha envío: {0} "
        return cadena.format(self.fechaGasto)
    
    class Meta:
        verbose_name: 'Gasto en envío: '
        verbose_name_plural: 'Gastos en envíos'
    
    def __str__ (self):
        return self.DatosGastoEnvio()
    
class GastoRemedio(models.Model):
    UNIT_CHOICES = [
        ('0', 'Kilogramos'),
        ('1', 'Litros'),
        ('2', 'Unidades'),
    ]
    fechaGasto = models.DateTimeField(blank=True,null=True,verbose_name="Gasto generado el:")
    RemediosPrecio=models.DecimalField(max_digits=7, decimal_places=2,blank=True)
    CantidadRemedios=models.DecimalField(max_digits=7, decimal_places=2,blank=True)
    unitRemedios = models.CharField(
        'unidad de medida',
        max_length=1,
        choices=UNIT_CHOICES,
        default='0',
    )
    proyecto = models.ForeignKey(Proyecto, verbose_name="Proyecto",blank=False,null=False, on_delete=models.CASCADE )
    created_at= models.DateTimeField(auto_now_add=True,blank=True, verbose_name="Creado el:")
    updated_at= models.DateTimeField(auto_now=True,blank=True, verbose_name="Actualizado el:")
    
    def DatosGastoRemedio(self):
        cadena = "Fecha de compra:{}0"
        return cadena.format(self.fechaGasto)
    
    class Meta:
        verbose_name: 'Gasto de consumo de remedios'
        verbose_name_plural: 'Gastos de consumo de remedios'
    
    def __str__ (self):
        return self.DatosGastoRemedio()
    
class GastoSemillas(models.Model):
    UNIT_CHOICES = [
        ('0', 'Kilogramos'),
        ('1', 'Litros'),
        ('2', 'Unidades'),
    ]
    fechaGasto = models.DateTimeField(blank=True,null=True,verbose_name="Gasto generado el:")
    TipoDeSemillas = models.CharField(max_length=50,blank=True)
    CantidadSemillas = models.DecimalField(max_digits=7, decimal_places=2, blank=True)
    unitSemillas = models.CharField(
        'unidad de medida',
        max_length=1,
        choices=UNIT_CHOICES,
        default='0',
        blank=True,
    )
    SemillasPrecio = models.DecimalField(max_digits=7, decimal_places=2, blank=True)
    proyecto = models.ForeignKey(Proyecto, verbose_name="Proyecto",blank=False,null=False, on_delete=models.CASCADE )
    created_at= models.DateTimeField(auto_now_add=True,blank=True, verbose_name="Creado el:")
    updated_at= models.DateTimeField(auto_now=True,blank=True, verbose_name="Actualizado el:")
    
    def DatosGastoSemillas(self):
        cadena = "Datos Consumo semillas: Tipo de cultivo:{0} Cantidad: {1},  Precio semillas: {2} "
        return cadena.format(self.TipoDeSemillas, self.CantidadSemillas, self.SemillasPrecio)
    
    class Meta:
        verbose_name: 'Gasto de consumo de semillas'
        verbose_name_plural: 'Gastos de consumo de semmillas'
    
    def __str__ (self):
        return self.DatosGastoSemillas()

class GastoCombustible(models.Model):    
    UNIT_CHOICES = [
        ('0', 'Kilogramos'),
        ('1', 'Litros'),
        ('2', 'Unidades'),
    ]
    fechaGasto = models.DateTimeField(blank=True,null=True,verbose_name="Gasto generado el:")
    CombustiblePrecio = models.DecimalField(max_digits=7, decimal_places=2, blank=True)
    CantidadCombustible = models.DecimalField(max_digits=7, decimal_places=2, blank=True)
    unitCombustible = models.CharField(
        'unidad de medida',
        max_length=30,
        choices=UNIT_CHOICES,
        default='0',
        blank=True, 
    )
    proyecto = models.ForeignKey(Proyecto, verbose_name="Proyecto",blank=False,null=False, on_delete=models.CASCADE )
    created_at= models.DateTimeField(auto_now_add=True,blank=True, verbose_name="Creado el:")
    updated_at= models.DateTimeField(auto_now=True,blank=True, verbose_name="Actualizado el:")
    
    def DatosGastoCombustible(self):
        cadena = "Datos Consumo combustible: Cantidad: {0},  Precio: {1} "
        return cadena.format(self.CantidadCombustible, self.CombustiblePrecio)
    
    class Meta:
        verbose_name: 'Gasto de consumo de combustible'
        verbose_name_plural: 'Gastos de consumo de combustible'
    
    def __str__ (self):
        return self.DatosGastoCombustible()

class GastoLimpieza(models.Model):
    UNIT_CHOICES = [
        ('0', 'Kilogramos'),
        ('1', 'Litros'),
        ('2', 'Unidades'),
    ]
    fechaGasto = models.DateTimeField(blank=True,null=True,verbose_name="Gasto generado el:")
    CantidadBasuraSolida= models.DecimalField(max_digits=7, decimal_places=2,blank=True)
    unitBasuraSolida = models.CharField(
        'unidad de medida',
        max_length=30,
        choices=UNIT_CHOICES,
        default='0',
    )
    RetiradaBasuraSolidaPrecio = models.DecimalField(max_digits=7, decimal_places=2,blank=True)
    CantidadLimpiezaAguasResiduales= models.DecimalField(max_digits=7, decimal_places=2,blank=True)
    unitLimpiezaAguasResiduales = models.CharField(
        'unidad de medida',
        max_length=30,
        choices=UNIT_CHOICES,
        default='0',
    )
    GastosLimpiezaAguasResiduales= models.DecimalField(max_digits=7, decimal_places=2,blank=True,default="0")
    proyecto = models.ForeignKey(Proyecto, verbose_name="Proyecto",blank=False,null=False, on_delete=models.CASCADE )
    created_at= models.DateTimeField(auto_now_add=True,blank=True, verbose_name="Creado el:")
    updated_at= models.DateTimeField(auto_now=True,blank=True, verbose_name="Actualizado el:")
    
    def DatosGastoLimpieza(self):
        cadena = "Fecha pago limpieza: {0}"
        return cadena.format(self.fechaGasto)
    
    class Meta:
        verbose_name: 'Gasto de limpieza'
        verbose_name_plural: 'Gastos de limpieza'
    
    def __str__ (self):
        return self.DatosGastoLimpieza()
    
class VariosGasto(models.Model):
    UNIT_CHOICES = [
        ('0', 'Kilogramos'),
        ('1', 'Litros'),
        ('2', 'Unidades'),
    ]
    
    GASTO_CHOICES = [
        ('0', 'Equipo de cultivo'),
        ('1', 'Ropa de trabajo'),
        ('2', 'Certificaciones'),
        ('3', 'Otros gastos'),
    ]
    
    
    VariosGasto = models.CharField(
        'gastos varios',
        max_length=1,
        choices=GASTO_CHOICES,
        default='0',
    )
    fechaGasto = models.DateTimeField(blank=True,null=True,verbose_name="Gasto generado el:")
    VariosGastoDescripcion = models.TextField(max_length=255, null=True,blank=True)
    VariosGastoCantidad = models.DecimalField(max_digits=7, decimal_places=2,blank=True)
    unitVariosGasto = models.CharField(
        'unidad de medida',
        max_length=1,
        choices=UNIT_CHOICES,
        default='0',
    )
    VariosGastoPrecio = models.DecimalField(max_digits=7, decimal_places=2,blank=True, default=0.0)
    proyecto = models.ForeignKey(Proyecto, verbose_name="Proyecto",blank=False,null=False, on_delete=models.CASCADE )
    created_at= models.DateTimeField(auto_now_add=True,blank=True, verbose_name="Creado el:")
    updated_at= models.DateTimeField(auto_now=True,blank=True, verbose_name="Actualizado el:")
    
    def DatosVariosGastos(self):
        cadena = "Datos Gastos Varios "
        return cadena
    
    class Meta:
        verbose_name: 'Gasto varios'
        verbose_name_plural: 'Gastos varios'
    
    def __str__ (self):
        return self.DatosVariosGastos()