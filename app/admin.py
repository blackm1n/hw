from django.contrib import admin
from .models import *


class ClientAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone']
    ordering = ['date_registered']
    list_filter = ['date_registered']
    search_fields = ['name']
    search_help_text = 'Search by name'

    fieldsets = [
        (
            None,
            {
                'classes': ['wide'],
                'fields': ['name']
            }
        ),
        (
            'Contact Info',
            {
                'fields': ['email', 'phone']
            }
        ),
        (
            'Address',
            {
                'classes': ['collapse'],
                'fields': ['address']
            }
        ),
        (
            'Date',
            {
                'fields': ['date_registered']
            }
        ),
    ]
    readonly_fields = ['date_registered']


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'count']
    ordering = ['date_created']
    list_filter = ['date_created', 'price', 'count']
    search_fields = ['name', 'description']
    search_help_text = 'Search by name and description'

    fieldsets = [
        (
            None,
            {
                'classes': ['wide'],
                'fields': ['name', 'image_tag']
            }
        ),
        (
            'Description',
            {
                'classes': ['collapse'],
                'fields': ['description']
            }
        ),
        (
            'Product Info',
            {
                'fields': ['price', 'count']
            }
        ),
        (
            'Date',
            {
                'fields': ['date_created']
            }
        ),
    ]
    readonly_fields = ['image_tag', 'date_created']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['client', 'total_price']
    ordering = ['date_ordered']
    list_filter = ['date_ordered', 'total_price']
    search_fields = ['client']
    search_help_text = 'Search by client'

    fieldsets = [
        (
            None,
            {
                'classes': ['wide'],
                'fields': ['client']
            }
        ),
        (
            'Order Info',
            {
                'fields': ['products', 'total_price']
            }
        ),
        (
            'Date',
            {
                'fields': ['date_ordered']
            }
        ),
    ]
    readonly_fields = ['date_ordered']


admin.site.register(Client, ClientAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
