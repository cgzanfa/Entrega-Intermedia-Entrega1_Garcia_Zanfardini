from django.db import models

# Create your models here.
class Cliente(models.Model):

    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    nro_cliente = models.IntegerField()


class Fruta(models.Model):

    fruta = models.CharField(max_length=30)
    precio = models.IntegerField()
    nro_articulo = models.IntegerField()


class Vegetal(models.Model):

    vegetal = models.CharField(max_length=30)
    precio = models.IntegerField()
    nro_articulo = models.IntegerField()


class Entregable(models.Model):
    nombre = models.CharField(max_length=100)
    fecha_de_entrega = models.DateField()
    entregado = models. BooleanField()

    def __str__(self):
        return f"{self.nombre} -> {self.fecha_de_entrega}"
    