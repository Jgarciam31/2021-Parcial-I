# Generated by Django 3.1.7 on 2021-03-14 07:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Producto', '0004_auto_20210314_0142'),
    ]

    operations = [
        migrations.RenameField(
            model_name='producto',
            old_name='categoria',
            new_name='categoriafk',
        ),
        migrations.RenameField(
            model_name='producto',
            old_name='marca',
            new_name='marcafk',
        ),
    ]
