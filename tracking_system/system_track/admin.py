from django.contrib import admin
from .models import Building, Technique


# Register your models here.
@admin.register(Building)
class BuildingAdmin(admin.ModelAdmin):
    pass


@admin.register(Technique)
class TechniqueAdmin(admin.ModelAdmin):
    pass