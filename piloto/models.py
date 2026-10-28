
from django.db import models
from auto.models import Auto


class Piloto(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    nacionalidad = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    numero = models.PositiveIntegerField()
    auto = models.ForeignKey(
        Auto,
        on_delete=models.PROTECT,
        related_name="pilotos"
    )

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

    class Meta:
        verbose_name = "Piloto"
        verbose_name_plural = "Pilotos"
