from django.db import models

# Create your models here.
class Turnover (models.Model):
    stockDays = models.PositiveSmallIntegerField(default=0);
    receivablesDays = models.PositiveSmallIntegerField(default=0);
    AccountsPayableDays = models.PositiveSmallIntegerField(default=0);
    stock=models.DecimalField(max_digits=7, decimal_places=2,blank=True)
    Receivables=models.DecimalField(max_digits=7, decimal_places=2,blank=True)
    Accounts=models.DecimalField(max_digits=7, decimal_places=2,blank=True)
    netWokingCap=models.DecimalField(max_digits=7, decimal_places=2,blank=True)
    ChangeOk=odels.DecimalField(max_digits=7, decimal_places=2,blank=True)

class group (models.Model):
    VATassets = models.DecimalField(max_digits=7, decimal_places=2,blank=True, verbose_name="VAT on purchased assets")
    VATreceivable=models.DecimalField(max_digits=7, decimal_places=2,blank=True, verbose_name="VAT receivable", verbose_name="Increase / (decrease) in VAT on purchased assets: ")
    IncDecVatAssets=models.DecimalField(max_digits=7, decimal_places=2,blank=True, verbose_name="Increase / (decrease) in VAT debt: ")
    IncDecVatDebt=models.DecimalField(max_digits=7, decimal_places=2,blank=True, verbose_name="Net working capital is the final: ")
    
    changeOk=models.DecimalField(max_digits=7, decimal_places=2,blank=True, verbose_name="Change OK: ")
    
    def Datosgroup(self):
        cadena = "Group Turnover:"
        return cadena.format(self.inflation, self.discountRate, self.grownRateFinal)
    
    class Meta:
        verbose_name: 'Group Operating capital: '
        verbose_name_plural: 'Group Operating Capitals: '
    
    def __str__ (self):
        return self.Datosgroup()