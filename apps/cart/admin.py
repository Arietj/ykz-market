from django.contrib import admin

# Register your models here.

from apps.cart.models import Cart, CartItem


admin.site.register(Cart)
admin.site.register(CartItem)
