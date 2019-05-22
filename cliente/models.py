from django.db import models


# Create your models here.
class Cliente(models.Model):
    nombre = models.CharField(
        max_length=150,
        null=False,
        blank=False,
        verbose_name="Nombre",
    )
    apellido_paterno = models.CharField(
        max_length=150,
        null=False,
        blank=False,
        verbose_name="Apellido Paterno"
    )
    apellido_materno = models.CharField(
        max_length=150,
        null=False,
        blank=False,
        verbose_name="Apellido Materno",
    )
    rfc = models.CharField(
        max_length=150,
        null=False,
        blank=False,
        verbose_name="RFC",
    )
    has_credito = models.BooleanField(
        verbose_name="¿Tiene crédito?",
        default=False,
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
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"

    def __str__(self):
        nombre_completo = self.nombre + " " + self.apellido_paterno + " " + self.apellido_materno

        return nombre_completo
