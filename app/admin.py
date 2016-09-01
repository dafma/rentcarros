from django.contrib import admin
from .models import Categorias, Equipamiento, Carro
# Register your models here.

@admin.register(Categorias)
class CategoriasAdmin(admin.ModelAdmin):
    search_fields = ("nombre",)
    list_filter = ("nombre",)
    pass

@admin.register(Equipamiento)
class EquipameintoAdmin(admin.ModelAdmin):
    search_fields = ("color",)
    list_filter = ("color",)
    list_display = ('cilindros', 'aire_acondicionado','electrico','transmicion','quemacocos','asientos_de_piel','gps','color', )
    pass



@admin.register(Carro)
class CarroAdmin(admin.ModelAdmin):
    search_fields = ("modelo",)
    list_filter = ("personas",)
    list_display = ('modelo', 'personas', 'imagen_principal', 'categoria', 'precio_por_dia',)
    pass
