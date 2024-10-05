from django.contrib import admin
from .models import Menu, MenuItem


# class to define inline tabular form of MenuItem model
class MenuItemInline(admin.TabularInline):
    model = MenuItem
    extra = 1


# register the Menu model with the Django admin site
@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    inlines = [MenuItemInline]
