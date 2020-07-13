from django.contrib import admin
from .models import Url


@admin.register(Url)
class UrlAdmin(admin.ModelAdmin):
    list_display = ["long_url", "short_url"]
    search_fields = ["long_url", "short_url"]
