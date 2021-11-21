from django.contrib import admin

from products.models import Product, ProductCategory

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('seller', 'category', 'name', 'brand', 'product_status', 'created_at')
    list_filter = ('category', 'seller', 'brand')
    search_fields = ('name',)


@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'depth', 'parent_category')
    list_filter = ('name', 'parent_category')
    search_fields = ('name',)
