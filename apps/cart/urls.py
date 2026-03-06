from rest_framework.routers import DefaultRouter
from apps.cart.views import CartViewSet, CartItemViewSet

default_router = DefaultRouter()

default_router.register('cart', CartViewSet, basename='cart')
default_router.register('cart-item', CartItemViewSet, basename='cart-item')