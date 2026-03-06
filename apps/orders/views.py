from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets, mixins, permissions, status
from apps.orders.serializers import OrderSerializer, OrderItemSerializer
from apps.orders.models import Order, OrderItem
from apps.cart.models import Cart, CartItem
# Create your views here.

class OrderViewSet(mixins.CreateModelMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)
    
    def create(self, request, *args, **kwargs):
        user = request.user
        cart, _ = Cart.objects.get_or_create(user=user)
        if not cart.items.exists():
            return Response({"detail": "Корзина пуста"}, status=status.HTTP_400_BAD_REQUEST)
        cart_items = cart.items.all()
        order = Order.objects.create(
            user=user,
            total_price=sum(item.product.price * item.quantity for item in cart_items)
        )
        order_items = [
            OrderItem(
                order=order,
                product=item.product,
                quantity=item.quantity,
                price=item.product.price
            ) for item in cart_items
        ]
        OrderItem.objects.bulk_create(order_items)

        # Очищаем корзину
        cart.items.all().delete()

        serializer = self.get_serializer(order)
        return Response(serializer.data)

    
class OrderItemViewSet(mixins.CreateModelMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer