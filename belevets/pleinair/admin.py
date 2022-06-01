from django.contrib import admin

from .models import PleinAir


@admin.register(PleinAir)
class PleinAirAdmin(admin.ModelAdmin):
    pass
