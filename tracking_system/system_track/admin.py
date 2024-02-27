from django.contrib import admin
from .models import Building, ChangeLog


# Register your models here.
@admin.register(Building)
class BuildingAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(ChangeLog)
class ChangeLogAdmin(admin.ModelAdmin):
    list_display = ['changed', 'model', 'user', 'record_id', 'data',
                    'ipaddress', 'action_on_model']
    readonly_fields = ['user']
    list_filter = ['model', 'action_on_model']
