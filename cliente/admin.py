from django.contrib import admin
from cliente.models import Cliente
from solicitud.models import Solicitud
from credito.models import Credito


# Register your models here.

class ClienteInline(admin.TabularInline):
    model = Solicitud

    extra = 1


class CreditoInline(admin.TabularInline):
    model = Credito

    extra = 1


class ClienteAdmin(admin.ModelAdmin):
    inlines = [
        ClienteInline,
        CreditoInline,
    ]

    list_display = (
        'nombre',
        'apellido_paterno',
        'apellido_materno',
        'rfc',
        'has_credito',
        'created_at',
        'updated_at',
    )

    exclude = (
        'codigo_credito',
        'solicitud',
    )

    search_fields = ['rfc']

admin.site.register(Cliente, ClienteAdmin)
