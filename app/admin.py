from django.contrib import admin

from django.contrib.auth.admin import UserAdmin
from .models import Grupo, Material

@admin.register(Grupo)
class GrupoAdmin(admin.ModelAdmin):
    pass

@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    pass