from django.contrib import admin
from cliente.models import Cliente


# Register your models here.
class ClienteAdmin(admin.ModelAdmin):

    list_display = (
        'nombre',
        'apellido_paterno',
        'apellido_materno',
        'rfc',
        'has_credito',
        'created_at',
        'updated_at',
    )

    search_fields = ['rfc']

admin.site.register(Cliente, ClienteAdmin)
