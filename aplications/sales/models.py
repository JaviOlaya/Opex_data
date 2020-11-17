from django.db import models

# Create your models here.
class SalesCrop(models.Model):
    UNITS =[
        ('0', 'kg'),
        ('1', 'Ton')
    ]
    
    
    inflation = models.DecimalField(max_digits=4, decimal_places=2,default="4.5")
    typeCrop = models.CharField(max_length=100, verbose_name="Crop type: ", blank=True)
    Productivity = models.DecimalField(max_digits=7, decimal_places=2,default="0")
    price = models.DecimalField(max_digits=4, decimal_places=2,default="0")
    revenues= models.DecimalField(max_digits=4, decimal_places=2,default="0")
    areaCrop = models.DecimalField(max_digits=4, decimal_places=2, default=0)