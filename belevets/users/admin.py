from django.contrib import admin

from .models import UserProfile, Order


@admin.register(UserProfile)
class AdminUserProfile(admin.ModelAdmin):
    pass


@admin.register(Order)
class AdminOrder(admin.ModelAdmin):
    list_display = ['id', 'date', 'payment']
