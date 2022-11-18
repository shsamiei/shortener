from django.contrib import admin
from . import models





@admin.register(models.Shortener)
class ShortenerAdmin(admin.ModelAdmin):
    list_display = ['url', 'shortener']

    