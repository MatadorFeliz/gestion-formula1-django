
from django.contrib import admin
from .models import Piloto


@admin.register(Piloto)
class PilotoAdmin(admin.ModelAdmin):
    list_display = (
        'nombre',
        'apellido',
        'nacionalidad',
        'numero',
        'auto',
    )

    search_fields = (
        'nombre',
        'apellido',
        'nacionalidad',
    )

    list_filter = ('nacionalidad', 'auto')

