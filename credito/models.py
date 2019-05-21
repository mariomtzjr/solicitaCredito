from django.db import models
from cliente.models import Cliente


# Create your models here.
class Credito(models.Model):
    codigo_credito = models.CharField(
        null=False,
        blank=False,
        max_length=150,
        verbose_name="Código de Crédito",
    )
    cliente = models.ForeignKey(
        Cliente,
        on_delete=models.CASCADE,
    )
    cantidad = models.FloatField(
        null=False,
        blank=False,
        verbose_name="Cantidad",
    )
    plazo = models.IntegerField(
        null=False,
        blank=False,
        verbose_name="Plazo (meses)",
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
        verbose_name = "Crédito"
        verbose_name_plural = "Créditos"

    def __str__(self):
        return self.codigo_credito
