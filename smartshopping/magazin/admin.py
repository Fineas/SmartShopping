from django.contrib import admin
from .models import LantMagazine

class LantMagazineAdmin(admin.ModelAdmin):
    list_display = ['nume']
    ordering = ['nume']

admin.site.register(LantMagazine, LantMagazineAdmin)
