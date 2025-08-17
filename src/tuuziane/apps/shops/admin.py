from django.contrib import admin
from .models import Shop


@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    list_display = ("name", "owner", "subdomain", "is_active", "created_at")
    list_filter = ("is_active",)
    search_fields = ("name", "subdomain", "owner__email")
    prepopulated_fields = {"subdomain": ("name",)}
