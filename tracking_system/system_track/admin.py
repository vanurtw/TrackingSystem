from django.contrib import admin
from .models import Building


# Register your models here.
@admin.register(Building)
class BuildingAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


