from django.contrib import admin
from .models import Colors

class ColorAdmin(admin.ModelAdmin):
    list_display = ("UI_ID", "NAME", "RGB", "SYMBOL", "USAGE_FOR_BRANDING", "CATEGORY", "MEANING")
    search_fields = ("NAME", "SYMBOL", "CATEGORY")  # Enables search by name, symbol, and category
    list_filter = ("CATEGORY", "USAGE_FOR_BRANDING")  # Adds filtering options in the admin panel
    ordering = ("UI_ID",)  # Orders records by UI_ID

admin.site.register(Colors, ColorAdmin)
