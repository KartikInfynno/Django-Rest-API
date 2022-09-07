from django.contrib import admin
from .models import ApiTest


@admin.register(ApiTest)
class ApiAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'age']
