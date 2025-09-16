# blog/admin.py

from django.contrib import admin
from .models import Product # Baris ini harus bisa menemukan 'Product' dari models.py

class ProductAdmin(admin.ModelAdmin):
    list_display = ('nama', 'harga', 'stok')
    search_fields = ('nama', 'deskripsi')
    list_filter = ('stok', 'harga')

admin.site.register(Product, ProductAdmin)