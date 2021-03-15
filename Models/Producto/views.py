from django.http import HttpRequest
from django.shortcuts import render

from Models.Producto.forms import formularioProducto, formularioMarca, formularioCategoria
from Models.Producto.models import Producto, Marca, Categoria


#PRODUCTOS


class FormularioProductoView(HttpRequest):

    def index(request):
        producto = formularioProducto()
        return render(request, "registrarProducto.html", {"form":producto})

    def procesarFormulario(request):
        producto = formularioProducto(request.POST)
        if producto.is_valid():
            producto.save()
            producto = formularioProducto()
        return render(request, "registrarProducto.html", {"form": producto, "mensaje": 'OK'})

    def listarProductos(request):
        productos = Producto.objects.all()
        return render(request, "listarProducto.html", {"productos": productos})

    def edit(request, id_producto):
        producto = Producto.objects.filter(id=id_producto).first()
        form = formularioProducto(instance=producto)
        return render(request, "editarProducto.html", {"form":form, "producto":producto})

    def actualizarProducto(request, id_producto):
        producto = Producto.objects.get(pk=id_producto)
        form = formularioProducto(request.POST, instance=producto)
        if form.is_valid():
            form.save()
        productos = Producto.objects.all()
        return render(request, "listarProducto.html", {"productos": productos})

    def eliminarProducto(request, id_producto):
        producto = Producto.objects.get(pk=id_producto)
        producto.delete()
        productos = Producto.objects.all()
        return render(request, "listarProducto.html", {"productos": productos})






#MARCAS


class FormularioMarcaView(HttpRequest):

    def index(request):
        marca = formularioMarca()
        return render(request, "registrarMarca.html", {"form":marca})

    def procesarMarca(request):
        marca = formularioMarca(request.POST)
        if marca.is_valid():
            marca.save()
            marca = formularioMarca()
        return render(request, "registrarMarca.html", {"form": marca, "mensaje": 'OK'})

    def listarMarca(request):
        marcas = Marca.objects.all()
        return render(request, "listarMarca.html", {"marcas": marcas})

    def edit(request, id_marca):
        marca = Marca.objects.filter(id=id_marca).first()
        form = formularioMarca(instance=marca)
        return render(request, "editarMarca.html", {"form":form, "marca":marca})

    def actualizarMarca(request, id_marca):
        marca = Marca.objects.get(pk=id_marca)
        form = formularioMarca(request.POST, instance=marca)
        if form.is_valid():
            form.save()
        marcas = Marca.objects.all()
        return render(request, "listarMarca.html", {"marcas": marcas})

    def eliminarMarca(request, id_marca):
        marca = Marca.objects.get(pk=id_marca)
        marca.delete()
        marcas = Marca.objects.all()
        return render(request, "listarMarca.html", {"marcas": marcas})








#CATEGORIAS


class FormularioCategoriaView(HttpRequest):

    def index(request):
        categoria = formularioCategoria()
        return render(request, "registrarCategoria.html", {"form":categoria})

    def procesarCategoria(request):
        categoria = formularioCategoria(request.POST)
        if categoria.is_valid():
            categoria.save()
            categoria = formularioMarca()
        return render(request, "registrarCategoria.html", {"form": categoria, "mensaje": 'OK'})

    def listarCategoria(request):
        categorias = Categoria.objects.all()
        return render(request, "listarCategoria.html", {"categorias": categorias})

    def edit(request, id_categoria):
        categoria = Categoria.objects.filter(id=id_categoria).first()
        form = formularioCategoria(instance=categoria)
        return render(request, "editarCategoria.html", {"form":form, "categoria":categoria})

    def actualizarCategoria(request, id_categoria):
        categoria = Categoria.objects.get(pk=id_categoria)
        form = formularioCategoria(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
        categorias= Categoria.objects.all()
        return render(request, "listarCategoria.html", {"categorias": categorias})

    def eliminarCategoria(request, id_categoria):
        categoria = Categoria.objects.get(pk=id_categoria)
        categoria.delete()
        categorias = Categoria.objects.all()
        return render(request, "listarCategoria.html", {"categorias": categorias})
