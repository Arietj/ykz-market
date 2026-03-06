from django.shortcuts import render
from rest_framework import viewsets, mixins, permissions
from apps.cart.models import Cart, CartItem
from apps.cart.serializers import CartSerializer, CartItemSerializer

class CartViewSet(mixins.CreateModelMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    serializer_class = CartSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Cart.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    
class CartItemViewSet(mixins.CreateModelMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    serializer_class = CartItemSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        cart, _ = Cart.objects.get_or_create(user=self.request.user)
        return CartItem.objects.filter(cart=cart)
    
    def perform_create(self, serializer):
        cart, _ = Cart.objects.get_or_create(user=self.request.user)
        serializer.save(cart=cart)