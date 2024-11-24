from django.contrib import admin
from .models import GrupoPersonalizado
# Register your models here.


@admin.register(GrupoPersonalizado)
class GrupoPersonalizadoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao')
    filter_horizontal = ('usuarios',)  # Facilita a seleção de usuários 
    