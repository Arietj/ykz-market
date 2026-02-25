from django.contrib import admin
from .models import Product, ProductImage, ProductSize, Size, Category, SubCategory


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1
    
    
class ProductSizeInline(admin.TabularInline):
    model = ProductSize
    extra = 1


# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'discount', 'price_with_discount', 'amount', 'created', 'updated', 'color', 'code', 'article', 'hit', 'promotion')
    list_filter = ('created', 'updated', 'color', 'hit', 'promotion', 'popular', 'sub_categories')
    search_fields = ('name', 'code', 'article', 'color')
    prepopulated_fields = {'slug': ('name',)}
    inlines = [ProductImageInline, ProductSizeInline]
    
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
    
class SizeAdmin(admin.ModelAdmin):
    list_display = ['name']
    
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'slug']
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(SubCategory, SubCategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Size, SizeAdmin)