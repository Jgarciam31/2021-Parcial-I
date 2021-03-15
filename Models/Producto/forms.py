from django import forms
from Models.Producto.models import Producto, Marca, Categoria


class formularioProducto(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'

class formularioMarca(forms.ModelForm):
    class Meta:
        model = Marca
        fields = '__all__'

class formularioCategoria(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = '__all__'