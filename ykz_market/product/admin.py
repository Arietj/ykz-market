from django.contrib import admin
from .models import Product, ProductImage, ProductDescription


# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass


@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    pass


@admin.register(ProductDescription)
class ProductDescriptionAdmin(admin.ModelAdmin):
    pass