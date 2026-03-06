from rest_framework import serializers
from apps.cart.models import Cart, CartItem
from apps.product.serializers import ProductSerializer


class CartItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    product_id = serializers.PrimaryKeyRelatedField(
        queryset=ProductSerializer.Meta.model.objects.all(), source='product', write_only=True
        )
    price = serializers.SerializerMethodField()

    class Meta:
        model = CartItem
        fields = ('id', 'product', 'product_id', 'quantity', 'price')


    def get_price(self, obj):
        return obj.product.price * obj.quantity

class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True, read_only=True)

    class Meta:
        model = Cart
        fields = ('id', 'user', 'created', 'updated', 'items')
        read_only_fields = ('user',)