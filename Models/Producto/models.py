from django.db import models


class Marca(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=75)

    def __str__(self):
        return self.nombre


class Categoria(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=75)

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=75)
    descripcion = models.CharField(max_length=200)
    preciocompra = models.IntegerField(primary_key=False)
    precioventa = models.IntegerField(primary_key=False)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE, name="Marca")
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, name="Categoria")














