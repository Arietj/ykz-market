from rest_framework.routers import DefaultRouter
from apps.orders.views import OrderViewSet, OrderItemViewSet

default_router = DefaultRouter()

default_router.register('order', OrderViewSet, basename='order')
default_router.register('order-item', OrderItemViewSet, basename='order-item')
