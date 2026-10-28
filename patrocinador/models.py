
from django.db import models
from piloto.models import Piloto


class Patrocinador(models.Model):
    nombre = models.CharField(max_length=100)
    sector = models.CharField(max_length=100)
    pais_origen = models.CharField(max_length=100)
    monto_aporte = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )
    piloto = models.ForeignKey(
        Piloto,
        on_delete=models.PROTECT,
        related_name="patrocinadores"
    )

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Patrocinador"
        verbose_name_plural = "Patrocinadores"

