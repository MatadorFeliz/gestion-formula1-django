
from django.contrib import admin
from .models import Auto


@admin.register(Auto)
class AutoAdmin(admin.ModelAdmin):
    list_display = (
        'nombre',
        'escuderia',
        'modelo',
        'motor',
        'temporada',
    )

    search_fields = (
        'nombre',
        'escuderia',
        'modelo',
    )

    list_filter = ('temporada', 'escuderia')

