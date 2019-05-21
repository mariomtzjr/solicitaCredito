from django.contrib import admin
from credito.models import Credito


# Register your models here.
class CreditoAdmin(admin.ModelAdmin):

    list_display = (
        'codigo_credito',
        'cliente',
        'cantidad',
        'plazo',
        'created_at',
        'updated_at',
    )

    search_fields = ['codigo_credito']

admin.site.register(Credito, CreditoAdmin)
