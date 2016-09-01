from django.db import models
from django.contrib.auth.models import User
from app.models import Carro
from django.core.validators import MaxValueValidator


class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=150)
    email = models.EmailField()
    num_tel = models.IntegerField('numero telefonico',)

# Create your models here.
class Reservacion(models.Model):
    cliente = models.ForeignKey(User)
    fecha_inicio = models.DateTimeField()
    fecha_termino = models.DateTimeField()
    carro = models.ForeignKey(Carro,)
    r_con = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Reservaciones"
        verbose_name_plural = "Reservaciones"

    def __str__(self):
        return self.cliente.username


class Tarjeta(models.Model):
    usuario = models.ForeignKey(User)
    num_tarjeta = models.IntegerField("Numero de tarjeta")
    codigo_cvc = models.PositiveIntegerField(validators=[MaxValueValidator(999)])
    fecha_expiracion = models.DateField()
    terminos_condiciones = models.BooleanField("Acepto politicas terminos y condiciones.")

    def __str__(self):
        return self.num_tarjeta