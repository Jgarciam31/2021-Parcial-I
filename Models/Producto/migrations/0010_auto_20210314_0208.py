# Generated by Django 3.1.7 on 2021-03-14 08:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Producto', '0009_auto_20210314_0205'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='categoria',
        ),
        migrations.RemoveField(
            model_name='producto',
            name='marca',
        ),
        migrations.AddField(
            model_name='producto',
            name='Categoria',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='Producto.categoria'),
        ),
        migrations.AddField(
            model_name='producto',
            name='Marca',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='Producto.marca'),
        ),
    ]
