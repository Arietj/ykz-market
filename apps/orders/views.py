from django.shortcuts import render
from rest_framework import viewsets, mixins
from apps.orders.serializers import OrderSerializer, OrderItemSerializer
from apps.orders.models import Order, OrderItem
# Create your views here.

class OrderViewSet(mixins.CreateModelMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrderItemViewSet(mixins.CreateModelMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer