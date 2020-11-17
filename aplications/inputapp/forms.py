from django import forms
from .models import Proyecto

class FormProyecto(forms.Form):
    model = Proyecto
    fields = (
        'nombre',
        'description',
        'total_area',
        'user',
        'fecha_inicio',
        'fecha_final',
        
    )
    
    widgets = {
        'nombre':forms.TextInput(
            attrs={
                'placeholder':'Name of the project',
                'class':'inputDjango',
            }
        ),
        'description':forms.Textarea(
            attrs={
                'placeholder':'Description of the project',
                'class':'textDjango',
            }
        ),
        'area_total':forms.NumberInput(
            attrs={
                'placeholder':'Area (m2)',
                'class':'areaProject',
            }
        ),
        'fecha_inicio':forms.DateInput(
            attrs={
                'class':'fechaDjango',
            }
        ),
        'fecha_final':forms.DateInput(
            attrs={
                'class':'fechaDjango',
            }
        ),
        'created_at':forms.DateInput(
            attrs={
                'class':'fechaDjango',
            }
        ),
        'updated_at':forms.DateInput(
            attrs={
                'class':'fechaDjango',
            }
        )
    }
    
    class FormPersonal(forms.Form):
        model = Proyecto
    fields = (
        'numero_empleados',
        'plantilla',
        'sueldo_empleados',
        'monedaBasurasolida',
        'proyecto',
        'fecha_final',
        
    )
    
    widgets = {
        'numero_empleados':forms.NumberInput(
            attrs={
                'placeholder':'Number of the employees',
                'class':'inputDjango',
            }
        ),
        'description':forms.Textarea(
            attrs={
                'placeholder':'Description of the project',
                'class':'textDjango',
            }
        ),
        'area_total':forms.NumberInput(
            attrs={
                'placeholder':'Area (m2)',
                'class':'areaProject',
            }
        ),
        'fecha_inicio':forms.DateInput(
            attrs={
                'class':'fechaDjango',
            }
        ),
        'fecha_final':forms.DateInput(
            attrs={
                'class':'fechaDjango',
            }
        ),
        'created_at':forms.DateInput(
            attrs={
                'class':'fechaDjango',
            }
        ),
        'updated_at':forms.DateInput(
            attrs={
                'class':'fechaDjango',
            }
        )
    }