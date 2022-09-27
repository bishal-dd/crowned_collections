from django.contrib import admin
from .models import Product, Order


class ProductAdmin(admin.ModelAdmin):
    list_display = ['product_name',  'price', 'stock']
    prepopulated_fields = {'slug': ('product_name',)}


class OrderAdmin(admin.ModelAdmin):
    list_display = ['product_name', 'FullName', 'phone_number', 'address']


admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)

