from django.db import models
from cliente.models import Cliente
from credito.models import Credito


# Create your models here.
class Solicitud(models.Model):
    num_solicitud = models.IntegerField(
        null=False,
        blank=False,
        verbose_name="Número de Solicitud",
    )
    cliente = models.ForeignKey(
        Cliente,
        on_delete=models.CASCADE,
    )
    credito = models.ForeignKey(
        Credito,
        on_delete=models.CASCADE,
    )
    created_at = models.DateTimeField(
        verbose_name="Fecha de creación",
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        verbose_name="Fecha de actualización",
        auto_now=True,
    )

    class Meta:
        verbose_name = "Solicitud"
        verbose_name_plural = "Solicitudes"

    def __str__(self):
        return self.num_solicitud
