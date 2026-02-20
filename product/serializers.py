from rest_framework import serializers
from product.models import *

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = ("id","category", "name", "product_count")

    def validate_name(self, value):
        if value[0].isupper():
            return value
        raise serializers.ValidationError("Invalid name")

class CategoryDetailSerializer(serializers.ModelSerializer):
    sub_categories = SubCategorySerializer(many=True, read_only=True)
    class Meta:
        model = Category
        fields = ('sub_categories',)

class ProductSerializer(serializers.ModelSerializer):
    category_detail = CategoryDetailSerializer(read_only=True)
    sub_categories = SubCategorySerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ('id', 'name', 'price', 'category_detail', 'sub_categories')

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

