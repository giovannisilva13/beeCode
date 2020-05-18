from django.contrib import admin

from products.models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = [
        'code', 'name', 'quantity', 'stock_exit', 'stock_entry', 'created_at',
    ]
    readonly_fields = [ 'quantity', ]
    
admin.site.register(Product, ProductAdmin)