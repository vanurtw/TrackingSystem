from django.contrib import admin
from .models import Tehnique


# Register your models here.


@admin.register(Tehnique)
class TehniqueAdmin(admin.ModelAdmin):
    list_display = ['name', 'inventory_number', 'building']
    list_editable = ['building']
