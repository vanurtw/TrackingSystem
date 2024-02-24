from django.contrib import admin
from .models import Tehnique


# Register your models here.


@admin.register(Tehnique)
class TehniqueAdmin(admin.ModelAdmin):
    list_display = ['name', 'inventory_number', 'building']
    readonly_fields = ['inventory_number']
    list_editable = ['building']
    list_filter = ['building', 'date_crete', 'status']
    search_fields = ['name', 'inventory_number']
