from rest_framework import serializers
from apps.orders.models import Order, OrderItem
from apps.product.serializers import ProductSerializer
from apps.product.serializers import SubCategorySerializer, CategorySerializer

class OrderItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    total_price = serializers.SerializerMethodField()
    product_name = serializers.SerializerMethodField()
    sub_category = SubCategorySerializer(read_only=True)
    category = CategorySerializer(read_only=True)

    class Meta:
        model = OrderItem
        fields = ('id', 'product', 'product_name', 'quantity', 'price', 'total_price')


    def get_product_name(self, obj):
        return obj.product.name
    

    def get_total_price(self, obj):
        price = obj.price if obj.price else obj.product.price
        return price * obj.quantity
    

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)
    total_order_price = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = ('id', 'user', 'status', 'created', 'changed', 'items', 'total_order_price')
        read_only_fields = ('user',)


    def get_total_order_price(self, obj):
        return sum(item.get_total_price() for item in obj.items.all())