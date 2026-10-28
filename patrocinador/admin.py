
from django.contrib import admin
from .models import Patrocinador


@admin.register(Patrocinador)
class PatrocinadorAdmin(admin.ModelAdmin):
    list_display = (
        'nombre',
        'sector',
        'pais_origen',
        'monto_aporte',
        'piloto',
    )

    search_fields = (
        'nombre',
        'sector',
        'piloto__nombre',
        'piloto__apellido',
    )

    list_filter = ('sector', 'pais_origen')

