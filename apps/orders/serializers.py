from rest_framework import serializers
from apps.orders.models import Order, OrderItem
from apps.product.serializers import ProductSerializer

class OrderItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    total_price = serializers.SerializerMethodField()

    class Meta:
        model = OrderItem
        fields = ('id', 'product', 'product_name', 'quantity', 'price', 'total_price')

    def get_total_price(self, obj):
        return obj.get_total_price()


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)  # все позиции заказа
    total_order_price = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = ('id', 'user', 'status', 'created', 'changed', 'items', 'total_order_price')
        read_only_fields = ('user',)

    def get_total_order_price(self, obj):
        return sum(item.get_total_price() for item in obj.items.all())