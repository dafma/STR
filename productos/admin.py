from django.contrib import admin
from .models import Producto, Categoria
# Register your models here.
"""
    @admin.register(TipoRenta)
class TipoRentaAdmin(admin.ModelAdmin):
    pass
"""



@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    pass

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    pass

