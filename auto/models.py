
from django.db import models


class Auto(models.Model):
    nombre = models.CharField(max_length=100)
    escuderia = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    motor = models.CharField(max_length=100)
    temporada = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.escuderia} - {self.modelo}"

    class Meta:
        verbose_name = "Auto"
        verbose_name_plural = "Autos"
