from django.contrib import admin
from .models import Reservacion, Tarjeta
# Register your models here.


@admin.register(Reservacion)
class ReservacionAdmin(admin.ModelAdmin):
    search_fields = ("clientes", )
    filter = ("carro")
    list_display = ('cliente', 'fecha_inicio', 'fecha_termino', 'carro')
    pass

@admin.register(Tarjeta)
class TarjetaAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'num_tarjeta', 'codigo_cvc', 'fecha_expiracion', 'terminos_condiciones')