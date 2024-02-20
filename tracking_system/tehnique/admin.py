from django.contrib import admin
from .models import Tehnique
# Register your models here.


@admin.register(Tehnique)
class TehniqueAdmin(admin.ModelAdmin):
    pass