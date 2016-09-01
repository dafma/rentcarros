#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.

class Categorias(models.Model):
    nombre = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Categorias"
        verbose_name_plural = "Categorias"

    def __str__(self):
        return self.nombre

TRANSMICIONES_CHOICE = (
    ('Au', 'Automatico'),
    ('Ma', 'Manual'),
    ('Tri', 'Tipronic'),
)

# SEXO_CHOICES=(
#     ('M', 'Masculino'),
#     ('F', 'Femenino'),
# )
DIRECCION_CHOICES = (
    ('Hidro', 'Hidraulica'),
    ('Asis','Asistida'),
)

class Equipamiento(models.Model):
    cilindros = models.SmallIntegerField()
    direccion = models.CharField("Dirección", max_length=5,choices=DIRECCION_CHOICES)
    aire_acondicionado = models.BooleanField()
    electrico = models.BooleanField()
    transmicion = models.CharField("Transmición", max_length=3, choices=TRANSMICIONES_CHOICE)
    quemacocos = models.BooleanField()
    asientos_de_piel = models.BooleanField()
    gps = models.BooleanField()
    color = models.CharField(max_length=50)

    def __str__(self):
        return self.color

    class Meta:
        verbose_name = "Equipamiento"
        verbose_name_plural = "Equipamiento"

# class Marca(models.Model):
#     nombre = models.CharField(max_length=50)
#
#     class Meta:
#         verbose_name = "Marca"
#         verbose_name_plural = "Marca"
#
#     def __str__(self):
#         return self.nombre

COMBUSTIBLE_CHOICES = (
    ('ds', 'Diesel'),
    ('gl','Gasolina'),
    ('hb', 'Hibrido'),
    ('gs','Gas'),
    ('el','Electrico'),
)

class Carro(models.Model):
    disponibilidad = models.BooleanField("Disponibilidad",default=True)
    modelo = models.CharField("Modelo", max_length=150)
    combustible = models.CharField(choices=COMBUSTIBLE_CHOICES, max_length=2, default="ds")
    anio = models.DateField("Año")
    verificacion = models.BooleanField("Verificación")
    personas = models.SmallIntegerField("Numero de Personas")
    imagen_principal = models.ImageField("Imagen Principal", blank=True, null=True)
    imagen_frontal = models.ImageField("Imagen Frontal", blank=True, null=True)
    imagen_lateral_izq = models.ImageField("Imagen Lateral Izquierda", blank=True, null=True)
    categoria = models.ForeignKey(Categorias)
    equipamiento = models.ForeignKey(Equipamiento)
    precio_por_dia = models.DecimalField(decimal_places=2, max_digits=15)

    class Meta:
        verbose_name = "Carros"
        verbose_name_plural = "Carros"

    def __str__(self):
        return self.modelo


