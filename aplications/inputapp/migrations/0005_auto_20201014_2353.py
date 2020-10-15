# Generated by Django 3.1.2 on 2020-10-14 23:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inputapp', '0004_gastocombustible'),
    ]

    operations = [
        migrations.AddField(
            model_name='gastosemillas',
            name='fechaGasto',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Gasto generado el:'),
        ),
        migrations.CreateModel(
            name='GastoLimpieza',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fechaGasto', models.DateTimeField(blank=True, null=True, verbose_name='Gasto generado el:')),
                ('CantidadBasuraSolida', models.DecimalField(blank=True, decimal_places=2, max_digits=7)),
                ('unitBasuraSolida', models.CharField(choices=[('0', 'Kilogramos'), ('1', 'Litros'), ('2', 'Unidades')], default='0', max_length=30, verbose_name='unidad de medida')),
                ('RetiradaBasuraSolidaPrecio', models.DecimalField(blank=True, decimal_places=2, max_digits=7)),
                ('CantidadLimpiezaAguasResiduales', models.DecimalField(blank=True, decimal_places=2, max_digits=7)),
                ('unitLimpiezaAguasResiduales', models.CharField(choices=[('0', 'Kilogramos'), ('1', 'Litros'), ('2', 'Unidades')], default='0', max_length=30, verbose_name='unidad de medida')),
                ('GastosLimpiezaAguasResiduales', models.DecimalField(blank=True, decimal_places=2, default='0', max_digits=7)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Creado el:')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Actualizado el:')),
                ('proyecto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inputapp.proyecto', verbose_name='Proyecto')),
            ],
        ),
    ]
