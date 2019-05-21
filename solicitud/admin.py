from django.contrib import admin
from solicitud.models import Solicitud


# Register your models here.
class SolicitudAdmin(admin.ModelAdmin):
    list_display = (
        'cod_solicitud',
        'cliente',
        'credito',
    )


admin.site.register(Solicitud, SolicitudAdmin)
