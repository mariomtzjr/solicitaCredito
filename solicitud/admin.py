from django.contrib import admin
from solicitud.models import Solicitud
from cliente.models import Cliente
from credito.models import Credito


# Register your models here.
# class ClienteInline(admin.TabularInline):
#    model = Cliente
#    list_display = (
#        'rfc',
#        'codigo_credito',
#        'created_at',
#        'updated_at',
#    )
#
#    search_fields = ['rfc', 'codigo_credito']
#
# class CreditoInline(admin.TabularInline):
#     model = Credito
#     list_display = (
#         'codigo_credito',
#         'cantidad',
#         'plazo',
#         'created_at',
#         'updated_at',
#     )
#
#     search_fields = ['codigo_credito']


class SolicitudAdmin(admin.ModelAdmin):
    # inlines = [ClienteInline, CreditoInline]

    readonly_fields = (
        'num_solicitud',
    )


admin.site.register(Solicitud, SolicitudAdmin)
