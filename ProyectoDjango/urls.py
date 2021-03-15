from django.contrib import admin
from django.urls import path

from Models.Producto.views import FormularioProductoView, FormularioMarcaView, FormularioCategoriaView
from Views.HomeView import HomeView

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', HomeView.home, name='home'),

    #Productos
    path('registrarProducto/', FormularioProductoView.index, name='registrarProducto'),
    path('guardarProducto/', FormularioProductoView.procesarFormulario, name='guardarProducto'),
    path('listarProducto/', FormularioProductoView.listarProductos, name='listarProducto'),
    path('editarProducto/<int:id_producto>', FormularioProductoView.edit, name='editarProducto'),
    path('actualizarProducto/<int:id_producto>', FormularioProductoView.actualizarProducto, name='actualizarProducto'),
    path('eliminarProducto/<int:id_producto>', FormularioProductoView.eliminarProducto, name='eliminarProducto'),

    #Marca
    path('registrarMarca/', FormularioMarcaView.index, name='registrarMarca'),
    path('guardarMarca/', FormularioMarcaView.procesarMarca, name='guardarMarca'),
    path('listarMarca/', FormularioMarcaView.listarMarca, name='listarMarca'),
    path('editarMarca/<int:id_marca>', FormularioMarcaView.edit, name='editarMarca'),
    path('actualizarMarca/<int:id_marca>', FormularioMarcaView.actualizarMarca, name='actualizarMarca'),
    path('eliminarMarca/<int:id_marca>', FormularioMarcaView.eliminarMarca, name='eliminarMarca'),

    #Categoria
    path('registrarCategoria/', FormularioCategoriaView.index, name='registrarCategoria'),
    path('guardarCategoria/', FormularioCategoriaView.procesarCategoria, name='guardarCategoria'),
    path('listarCategoria/', FormularioCategoriaView.listarCategoria, name='listarCategoria'),
    path('editarCategoria/<int:id_categoria>', FormularioCategoriaView.edit, name='editarCategoria'),
    path('actualizarCategoria/<int:id_categoria>', FormularioCategoriaView.actualizarCategoria, name='actualizarCategoria'),
    path('eliminarCategoria/<int:id_categoria>', FormularioCategoriaView.eliminarCategoria, name='eliminarCategoria'),


]
