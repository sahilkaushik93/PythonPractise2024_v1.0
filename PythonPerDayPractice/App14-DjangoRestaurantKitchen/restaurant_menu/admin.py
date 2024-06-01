from django.contrib import admin
from .models import Item

# Register your models here.
class MenuItemAdmin(admin.ModelAdmin):
    # "meal", "status", "description" they are defined in "models.py/Item"
    list_display = ("meal", "status")
    list_filter = ("status",)
    search_fields = ("meal", "description")


admin.site.register(Item, MenuItemAdmin)







