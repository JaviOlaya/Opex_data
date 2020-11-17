from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.urls import reverse
# Create your models here.

class Proyecto(models.Model):
    
    nombre= models.CharField(max_length=50, verbose_name="Name")
    description= models.TextField(max_length=300, blank=True,verbose_name="Description")
    area_total = models.DecimalField(max_digits=7, decimal_places=2,blank=True,default=0,verbose_name="Area(m2): ")
    fecha_inicio= models.DateField(blank=True, verbose_name="Start date: ")
    fecha_final= models.DateField(blank=True,null=True, verbose_name="Finish date: ")
    created_at= models.DateField(auto_now_add=True, verbose_name="Created at:")
    updated_at= models.DateField(auto_now=True, verbose_name="Updated at:")
    user= models.ForeignKey(User, blank=False, null=False, on_delete=models.CASCADE, default=0)
   
    
    class Meta:
        verbose_name="Project"
        verbose_name_plural="Projects"
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.nombre)
        super(Proyecto, self).save(*args, **kwargs)
    
    def DatosProyecto(self):
        cadena="{0}"
        return cadena.format(self.nombre)

    def __str__ (self):
        return self.DatosProyecto()
    
class Personal(models.Model):
    UNIT_PRICE =[
        ('0', '€'),
        ('1', '€/kg'),
        ('2', 'x1000€/Mo.'),
    ]
    DEPARTAMENT_CHOICES = [
        ('Manager', 'Manager'),
        ('Commercial', 'Commercial'),
        ('Administrative', 'Administrative'),
        ('Support', 'Support')
    ]
    numero_empleados = models.PositiveSmallIntegerField()
    plantilla =models.CharField(
        verbose_name="Departament",
        max_length=30,
        choices=DEPARTAMENT_CHOICES,default='Manager',
    )
    sueldo_empleado = models.DecimalField(max_digits=7, decimal_places=2,blank=True)
    monedaBasuraSolida = models.CharField(
        'money parameter',
        max_length=30,
        choices=UNIT_PRICE,
        default='0',
    )
    proyecto = models.ForeignKey(Proyecto,blank=False,null=False, on_delete=models.CASCADE ,verbose_name="Project: ")
    created_at= models.DateField(auto_now_add=True, verbose_name="Created at:")
    updated_at= models.DateField(auto_now=True, verbose_name="Updated at:")
 
        
    class Meta:
        verbose_name="Personal"
        verbose_name_plural ="Personal"
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.proyecto.nombre)
        super(Personal, self).save(*args, **kwargs)
        
    def DatosPersonal(self):
        cadena = "Department employee data: {0}, of the project: {1}"
        return cadena.format(self.plantilla, self.proyecto.nombre)
        
    def __str__ (self):
        return self.DatosPersonal()        

#Desde aquí empiezan los gastos

class GastoAdministrativo(models.Model):
    UNIT_PRICE =[
        ('0', '€'),
        ('1', '€/kg'),
        ('2', 'x1000€/Mo.'),
    ]
    GADMIN_CHOICES = [
        ('0', 'Agronomy consulting'),
        ('1', 'Education'),
        ('2', 'Training'),
        ('3', 'POL on administrative needs'),
        ('4', 'Office expenses'),
        ('5', 'Households costs. needs'),
        ('6', 'Entertainment expenses'),
        ('7', 'Travel expenses'),
        ('8', 'Information Services'),
        ('9', 'Property insurance'),
    ]
    Descripcion = models.TextField(max_length=200,blank=False)
    cantidadGasto = models.DecimalField(max_digits=7, decimal_places=2,blank=True, default='0')
    monedaBasuraSolida = models.CharField(
        'money parameter',
        max_length=30,
        choices=UNIT_PRICE,
        default='0',
    )
    TipoGasto = models.CharField(max_length=1,choices=GADMIN_CHOICES,default='0')
    fecha_gasto = models.DateField(blank=True,null=True,verbose_name="Expense generated on:")  
    proyecto = models.ForeignKey(Proyecto,blank=False,null=False, on_delete=models.CASCADE ,verbose_name="Project: ")
    created_at= models.DateField(auto_now_add=True, verbose_name="Created at:")
    updated_at= models.DateField(auto_now=True, verbose_name="Updated at:")
    
    
    def DatosGastoAdministrativo(self):
        cadena = "Expense: {0}, Date:{1}"
        return cadena.format(self.TipoGasto, self.fecha_gasto)
    
    class Meta:
        verbose_name: 'Administrative Expense'
        verbose_name_plural: 'Administrative expenses'
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.proyecto.nombre)
        super(GastoAdministrativo, self).save(*args, **kwargs)
    
    def __str__ (self):
        return self.DatosGastoAdministrativo()

class GastoElectrico(models.Model):
    UNIT_PRICE =[
        ('0', '€'),
        ('1', '€/kg'),
        ('2', 'x1000€/Mo.'),
    ]
    UNIT_CHOICES = [
        ('0', 'Kg/m2'),
        ('1', 'L/m2'),
        ('2', 'Units/m2'),
    ]
    fechaGasto = models.DateField(blank=True,null=True,verbose_name="Expense generated on:")
    
    CantidadPotElec = models.DecimalField(max_digits=7, decimal_places=2,blank=True, verbose_name="Electric quantity: ")
    unitPotElec = models.CharField(
        'unit of measurement',
        max_length=1,
        choices=UNIT_CHOICES, 
        default='0',
    )
    PotElectricaPrecio = models.DecimalField(max_digits=7, decimal_places=2,blank=True, verbose_name="Electric price: ")
    monedaBasuraSolida = models.CharField(
        'money parameter',
        max_length=30,
        choices=UNIT_PRICE,
        default='0',
    )
    proyecto = models.ForeignKey(Proyecto,blank=False,null=False, on_delete=models.CASCADE ,verbose_name="Project: ")
    created_at =models.DateField(auto_now_add=True, verbose_name="Created at:")
    updated_at =models.DateField(auto_now=True, verbose_name="Updated at: ")
   
    
    def DatosGastoElectrico(self):
        cadena = "Date:{0}"
        return cadena.format(self.fechaGasto)
    
    class Meta:
        verbose_name: 'Electric expense'
        verbose_name_plural: 'Electric expenses'
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.proyecto.nombre)
        super(GastoElectrico, self).save(*args, **kwargs)
    
    
    def __str__ (self):
        return self.DatosGastoElectrico()

class GastoGas(models.Model):
    UNIT_PRICE =[
        ('0', '€'),
        ('1', '€/kg'),
        ('2', 'x1000€/Mo.'),
    ]
    UNIT_CHOICES = [
        ('0', 'Kg/m2'),
        ('1', 'L/m2'),
        ('2', 'Units/m2'),
    ]      
    fechaGasto = models.DateField(blank=True,null=True,verbose_name="Expense generated on:")
    CantidadGas = models.DecimalField(max_digits=7, decimal_places=2,blank=True)
    unitGas = models.CharField(
        'unit of measurement',
        max_length=1,
        choices=UNIT_CHOICES, 
        default='0',
    )
    PrecioGas = models.DecimalField(max_digits=7, decimal_places=2,blank=True)
    monedaBasuraSolida = models.CharField(
        'money parameter',
        max_length=30,
        choices=UNIT_PRICE,
        default='0',
    )
    proyecto = models.ForeignKey(Proyecto, blank=False,null=False, on_delete=models.CASCADE ,verbose_name="Project: ")
    created_at =models.DateField(auto_now_add=True, verbose_name="Created at:")
    updated_at =models.DateField(auto_now=True, verbose_name="Updated at: ")

    
    def DatosGastoGas(self):
        cadena = "Gas Consumption Data:  consumption: {0},  Gas price: {1} "
        return cadena.format(self.CantidadGas, self.PrecioGas)
    
    class Meta:
        verbose_name: 'Gas consumption expense'
        verbose_name_plural: 'Gas consumption expenses'
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.proyecto.nombre)
        super(GastoGas, self).save(*args, **kwargs)
    
    def __str__ (self):
        return self.DatosGastoGas()
    
class GastoFertilizante(models.Model):
    UNIT_PRICE =[
        ('0', '€'),
        ('1', '€/kg'),
        ('2', 'x1000€/Mo.'),
    ]
    UNIT_CHOICES = [
        ('0', 'Kg/m2'),
        ('1', 'L/m2'),
        ('2', 'Units/m2'),   
    ]    
    fechaGasto = models.DateField(blank=True,null=True,verbose_name="Expense generated on:")
    CantidadFertilizante = models.DecimalField(max_digits=7,decimal_places=2,blank=True, verbose_name="Fertilizer quantity: ")
    unitFertilizante = models.CharField(
        'unit of measurement',
        max_length=1,
        choices=UNIT_CHOICES, 
        default='0',
    )
    FertilizantePrecio = models.DecimalField(max_digits=7, decimal_places=2,blank=True,null=True, verbose_name=" Fertilizer Price: ")
    monedaBasuraSolida = models.CharField(
        'money parameter',
        max_length=30,
        choices=UNIT_PRICE,
        default='0',
    )
    proyecto = models.ForeignKey(Proyecto,blank=False,null=False, on_delete=models.CASCADE ,verbose_name="Project: ")
    created_at= models.DateField(auto_now_add=True,blank=True, verbose_name="Created at:")
    updated_at= models.DateField(auto_now=True,blank=True, verbose_name="Updated at:")


    def DatosGastoFertilizante(self):
        cadena = "Expense date: {0} "
        return cadena.format(self.fechaGasto)
    
    class Meta:
        verbose_name: 'Fertilizer consumption expenditure'
        verbose_name_plural: 'Fertilizer consumption expenditures'
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.proyecto.nombre)
        super(GastoFertilizante, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.DatosGastoFertilizante()

class GastoSubstrato(models.Model):
    UNIT_PRICE =[
        ('0', '€'),
        ('1', '€/kg'),
        ('2', 'x1000€/Mo.'),
    ]
    UNIT_CHOICES = [
        ('0', 'Kg/m2'),
        ('1', 'L/m2'),
        ('2', 'Units/m2'),
    ]
    fechaGasto = models.DateField(blank=True,null=True,verbose_name="Expense generated on:")
    SubstratoPrecio = models.DecimalField(max_digits=7, decimal_places=2,blank=True, verbose_name="Substrate price:")
    monedaBasuraSolida = models.CharField(
        'money parameter',
        max_length=30,
        choices=UNIT_PRICE,
        default='0',
    )
    CantidadSubstrato = models.DecimalField(max_digits=7, decimal_places=2,blank=True, verbose_name="Substrate quantity: ")
    unitSubstrato = models.CharField(
        'unit of measurement',
        max_length=1,
        choices=UNIT_CHOICES, 
        default='0',
    )
    proyecto = models.ForeignKey(Proyecto,blank=False,null=False, on_delete=models.CASCADE ,verbose_name="Project: ")
    created_at= models.DateField(auto_now_add=True,blank=True, verbose_name="Created at:")
    updated_at= models.DateField(auto_now=True,blank=True, verbose_name="Updated at:")
 
    
    def DatosGastoSubstrato(self):
        cadena = "Substrate consumption data: Consumption: {0},  Substrate price: {1} "
        return cadena.format(self.CantidadSubstrato, self.SubstratoPrecio)
    
    class Meta:
        verbose_name: 'Substrate consumption expenditure'
        verbose_name_plural: 'Substrate consumption expenditures'
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.proyecto.nombre)
        super(GastoSubstrato, self).save(*args, **kwargs)
    
    def __str__ (self):
        return self.DatosGastoSubstrato()
    
class GastoEnvio(models.Model):
    UNIT_PRICE =[
        ('0', '€'),
        ('1', '€/kg'),
        ('2', 'x1000€/Mo.'),
    ]
    fechaGasto = models.DateField(blank=True,null=True,verbose_name="Expense generated on:")
    descripcion = models.TextField(max_length=200,blank=True,verbose_name="Description: ") 
    EnvioPrecio = models.DecimalField(max_digits=7, decimal_places=2,blank=False,verbose_name="Shipping price: ")
    monedaBasuraSolida = models.CharField(
        'money parameter',
        max_length=30,
        choices=UNIT_PRICE,
        default='0',
    )
    proyecto = models.ForeignKey(Proyecto,blank=False,null=False, on_delete=models.CASCADE ,verbose_name="Project: ")
    created_at= models.DateField(auto_now_add=True,blank=True, verbose_name="Created at:")
    updated_at= models.DateField(auto_now=True,blank=True, verbose_name="Updated at:")
 
    
    def DatosGastoEnvio(self):
        cadena = "Shipping date: {0} "
        return cadena.format(self.fechaGasto)
    
    class Meta:
        verbose_name: 'Shipping cost: '
        verbose_name_plural: 'Shipping cost:'
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.proyecto.nombre)
        super(GastoEnvio, self).save(*args, **kwargs)
    
    
    def __str__ (self):
        return self.DatosGastoEnvio()
    
class GastoRemedio(models.Model):
    UNIT_PRICE =[
        ('0', '€'),
        ('1', '€/kg'),
        ('2', 'x1000€/Mo.'),
    ]
    UNIT_CHOICES = [
        ('0', 'Kg/m2'),
        ('1', 'L/m2'),
        ('2', 'Units/m2'),
    ]
    fechaGasto = models.DateField(blank=True,null=True,verbose_name="Expense generated on:")
    RemediosPrecio=models.DecimalField(max_digits=7, decimal_places=2,blank=True, verbose_name="Remedies price: ")
    monedaBasuraSolida = models.CharField(
        'money parameter',
        max_length=30,
        choices=UNIT_PRICE,
        default='0',
    )
    CantidadRemedios=models.DecimalField(max_digits=7, decimal_places=2,blank=True, verbose_name="Remedies quantity")
    unitRemedios = models.CharField(
        'unit of measurement',
        max_length=1,
        choices=UNIT_CHOICES,
        default='0',
    )
    proyecto = models.ForeignKey(Proyecto,blank=False,null=False, on_delete=models.CASCADE ,verbose_name="Project: ")
    created_at= models.DateField(auto_now_add=True,blank=True, verbose_name="Created at:")
    updated_at= models.DateField(auto_now=True,blank=True, verbose_name="Updated at:")
 
    
    def DatosGastoRemedio(self):
        cadena = "Date of purchase: {0}"
        return cadena.format(self.fechaGasto)
    
    class Meta:
        verbose_name: 'Medicine consumption expenditure'
        verbose_name_plural: 'Medicine consumption expenditures'
    
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.proyecto.nombre)
        super(GastoRemedio, self).save(*args, **kwargs)
    
    def __str__ (self):
        return self.DatosGastoRemedio()
    
class GastoSemillas(models.Model):
    UNIT_PRICE =[
        ('0', '€'),
        ('1', '€/kg'),
        ('2', 'x1000€/Mo.'),
    ]
    UNIT_CHOICES = [
        ('0', 'Kg/m2'),
        ('1', 'L/m2'),
        ('2', 'Units/m2'),
    ]
    fechaGasto = models.DateField(blank=True,null=True,verbose_name="Expense generated on:")
    TipoDeSemillas = models.TextField(max_length=250,blank=True, verbose_name="Seed type: ")
    CantidadSemillas = models.DecimalField(max_digits=7, decimal_places=2, blank=True,verbose_name="Seeds quantity")
    unitSemillas = models.CharField(
        'unit of measurement',
        max_length=1,
        choices=UNIT_CHOICES,
        default='0',
        blank=True,
    )
    SemillasPrecio = models.DecimalField(max_digits=7, decimal_places=2, blank=True, verbose_name="Seeds price: ")
    monedaBasuraSolida = models.CharField(
        'money parameter',
        max_length=30,
        choices=UNIT_PRICE,
        default='0',
    ) 
    proyecto = models.ForeignKey(Proyecto,blank=False,null=False, on_delete=models.CASCADE ,verbose_name="Project: ")
    created_at= models.DateField(auto_now_add=True,blank=True, verbose_name="Created at:")
    updated_at= models.DateField(auto_now=True,blank=True, verbose_name="Updated at:")
   
    
    def DatosGastoSemillas(self):
        cadena = "Seed consumption data: Type of crop:{0} Quantity: {1},  Seed price: {2} "
        return cadena.format(self.TipoDeSemillas, self.CantidadSemillas, self.SemillasPrecio)
    
    class Meta:
        verbose_name: 'Seed consumption expenditure'
        verbose_name_plural: 'Seed consumption expenditures'
    
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.proyecto.nombre)
        super(GastoSemillas, self).save(*args, **kwargs)
    
    def __str__ (self):
        return self.DatosGastoSemillas()

class GastoCombustible(models.Model):
    UNIT_PRICE =[
        ('0', '€'),
        ('1', '€/kg'),
        ('2', 'x1000€/Mo.'),
    ]    
    UNIT_CHOICES = [
        ('0', 'Kg/m2'),
        ('1', 'L/m2'),
        ('2', 'Units/m2'),
    ]
    fechaGasto = models.DateField(blank=True,null=True,verbose_name="Expense generated on:")
    CombustiblePrecio = models.DecimalField(max_digits=7, decimal_places=2, blank=True, verbose_name="Fuel price: ")
    monedaBasuraSolida = models.CharField(
        'money parameter',
        max_length=30,
        choices=UNIT_PRICE,
        default='0',
    )
    CantidadCombustible = models.DecimalField(max_digits=7, decimal_places=2, blank=True, verbose_name="Fuel Quantity: ")
    unitCombustible = models.CharField(
        'unit of measurement',
        max_length=30,
        choices=UNIT_CHOICES,
        default='0',
        blank=True, 
    )
    proyecto = models.ForeignKey(Proyecto,blank=False,null=False, on_delete=models.CASCADE ,verbose_name="Project: ")
    created_at= models.DateField(auto_now_add=True,blank=True, verbose_name="Created at:")
    updated_at= models.DateField(auto_now=True,blank=True, verbose_name="Updated at:")
    
    
    def DatosGastoCombustible(self):
        cadena = "Fuel consumption data: Quantity: {0},  Fuel price: {1} "
        return cadena.format(self.CantidadCombustible, self.CombustiblePrecio)
    
    class Meta:
        verbose_name: 'Fuel consumption expense'
        verbose_name_plural: 'Fuel consumption expenses'
    
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.proyecto.nombre)
        super(GastoCombustible, self).save(*args, **kwargs)
    
    def __str__ (self):
        return self.DatosGastoCombustible()

class GastoLimpieza(models.Model):
    UNIT_PRICE =[
        ('0', '€'),
        ('1', '€/kg'),
        ('2', 'x1000€/Mo.'),
    ]
    UNIT_CHOICES = [
        ('0', 'Kg/m2'),
        ('1', 'L/m2'),
        ('2', 'Units/m2'),
    ]
    fechaGasto = models.DateField(blank=True,null=True,verbose_name="Expense generated on:")
    CantidadBasuraSolida= models.DecimalField(max_digits=7, decimal_places=2,blank=True, verbose_name="solid garbage quantity: ")
    unitBasuraSolida1 = models.CharField(
        'unit of measurement',
        max_length=30,
        choices=UNIT_CHOICES,
        default='0',
    )
    RetiradaBasuraSolidaPrecio = models.DecimalField(max_digits=7, decimal_places=2,blank=True,verbose_name="solid garbage price: ")
    monedaBasuraSolida = models.CharField(
        'money parameter',
        max_length=30,
        choices=UNIT_PRICE,
        default='0',
    )
    
    CantidadLimpiezaAguasResiduales= models.DecimalField(max_digits=7, decimal_places=2,blank=True, default=0,verbose_name='Wastewater quantity:')
    unitLimpiezaAguasResiduales = models.CharField(
        'unit of measurement',
        max_length=30,
        choices=UNIT_CHOICES,
        default='0',
    )
    GastosLimpiezaAguasResiduales= models.DecimalField(max_digits=7, decimal_places=2,blank=True,default="0", verbose_name="Wastewater price: ")
    monedaBasuraSolida = models.CharField(
        'money parameter',
        max_length=30,
        choices=UNIT_PRICE,
        default='0',
    )
    proyecto = models.ForeignKey(Proyecto,blank=False,null=False, on_delete=models.CASCADE ,verbose_name="Project: ")
    created_at= models.DateField(auto_now_add=True,blank=True, verbose_name="Created at:")
    updated_at= models.DateField(auto_now=True,blank=True, verbose_name="Updated at:")
    
    
    def DatosGastoLimpieza(self):
        cadena = "Cleaning payment date: {0}"
        return cadena.format(self.fechaGasto)
    
    class Meta:
        verbose_name: 'Cleaning cost'
        verbose_name_plural: 'Cleaning costs'
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.proyecto.nombre)
        super(GastoLimpieza, self).save(*args, **kwargs)
    
    
    def __str__ (self):
        return self.DatosGastoLimpieza()
    
class VariosGasto(models.Model):
    UNIT_PRICE =[
        ('0', '€'),
        ('1', '€/kg'),
        ('2', 'x1000€/Mo.'),
    ]
    UNIT_CHOICES = [
        ('0', 'Kg/m2'),
        ('1', 'L/m2'),
        ('2', 'Units/m2'),
    ]
    
    GASTO_CHOICES = [
        ('0', 'Cultivation equipment'),
        ('1', 'Overall'),
        ('2', 'Certifications'),
        ('3', 'Other expenses'),
    ]
    
    
    VariosGasto = models.CharField(
        'Miscellaneous expenses',
        max_length=1,
        choices=GASTO_CHOICES,
        default='0',
    )
    fechaGasto = models.DateField(blank=True,null=True,verbose_name="Expense generated on:")
    VariosGastoDescripcion = models.TextField(max_length=255, null=True,blank=True, verbose_name="Description: ")
    VariosGastoCantidad = models.DecimalField(max_digits=7, decimal_places=2,blank=True, verbose_name="Quantity: ")
    unitVariosGasto = models.CharField(
        'unit of measurement',
        max_length=1,
        choices=UNIT_CHOICES,
        default='0',
    )
    VariosGastoPrecio = models.DecimalField(max_digits=7, decimal_places=2,blank=True, default=0, verbose_name="Price")
    monedaBasuraSolida = models.CharField(
        'money parameter',
        max_length=30,
        choices=UNIT_PRICE,
        default='0',
    )
    proyecto = models.ForeignKey(Proyecto, blank=False,null=False, on_delete=models.CASCADE ,verbose_name="Project: ")
    created_at= models.DateField(auto_now_add=True,blank=True, verbose_name="Created at:")
    updated_at= models.DateField(auto_now=True,blank=True, verbose_name="Updated at:")
 
    
    def DatosVariosGastos(self):
        cadena = "Miscellaneous expense data: Quantity: {0}, Price {1} "
        return cadena.format(self.VariosGastoCantidad, self.VariosGastoPrecio)
    
    class Meta:
        verbose_name: 'Miscellaneous expense'
        verbose_name_plural: 'Miscellaneous expenses'
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.proyecto.nombre)
        super(VariosGasto, self).save(*args, **kwargs)
    
    def __str__ (self):
        return self.DatosVariosGastos()

class taxRate(models.Model):
    proyecto = models.ForeignKey(Proyecto,blank=False,null=False, on_delete=models.CASCADE ,verbose_name="Project: ") 
    vatOutgoing=models.DecimalField(max_digits=5, decimal_places=2,blank=True, verbose_name="VAT-outgoing: ")
    vatIncluded=models.DecimalField(max_digits=5, decimal_places=2,blank=True, verbose_name="VAT-included: ")
    propertyTax=models.DecimalField(max_digits=5, decimal_places=2,blank=True, verbose_name="Property Tax: ")
    landTax=models.DecimalField(max_digits=5, decimal_places=2,blank=True, verbose_name="Land Tax: ")
    taxOnProfits=models.DecimalField(max_digits=5, decimal_places=2,blank=True, verbose_name="Tax on profits: ")
    socSecContributions=models.DecimalField(max_digits=7, decimal_places=2,blank=True, verbose_name="Social security contributions: ")
    created_at= models.DateField(auto_now_add=True,blank=True, verbose_name="Created at:")
    updated_at= models.DateField(auto_now=True,blank=True, verbose_name="Updated at:")
 
    def DatostaxRate(self):
        cadena = "Tax rate "
        return cadena.format()
    
    class Meta:
        verbose_name: 'Tax rate'
        verbose_name_plural: 'Tax rates'
    
    def __str__ (self):
        return self.DatostaxRate()
    
class macroeconomicsIndicators(models.Model):
    proyecto = models.ForeignKey(Proyecto,blank=False,null=False, on_delete=models.CASCADE ,verbose_name="Project: ")
    inflation = models.DecimalField(max_digits=7, decimal_places=2,blank=True, verbose_name="Inflation per Country: ")
    discountRate=models.DecimalField(max_digits=7, decimal_places=2,blank=True, verbose_name="Discount rate: ")
    grownRateFinal= models.DecimalField(max_digits=7, decimal_places=2,blank=True, verbose_name="The grown rate of the final cash flow: ")
    created_at= models.DateField(auto_now_add=True,blank=True, verbose_name="Created at:")
    updated_at= models.DateField(auto_now=True,blank=True, verbose_name="Updated at:")
 
    
    def DatosmacroeconomicsIndicators(self):
        cadena = "Macroeconomic indicators: {0}, {1}, {2} "
        return cadena.format(self.inflation, self.discountRate, self.grownRateFinal)
    
    class Meta:
        verbose_name: 'Macroeconomic indicator'
        verbose_name_plural: 'Macroeconomic indicators'
    
    def __str__ (self):
        return self.DatosmacroeconomicsIndicators()