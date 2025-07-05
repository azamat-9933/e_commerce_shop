from rest_framework import serializers

from cart.models import Cart, CartItem
from store.serializers import ProductCardSerializer

class CartItemSerializer(serializers.ModelSerializer):
    product = ProductCardSerializer(read_only=True)
    product_id = serializers.IntegerField(write_only=True, help_text="Product ID")
    item_cost = serializers.SerializerMethodField()


    class Meta:
        model = CartItem
        fields = ('id', 'product', 'product_id', 'quantity', 'added_at', 'item_cost')
        read_only_fields = ('id', 'item_cost', 'product')

    def get_item_cost(self, obj):
        return obj.get_cost()

class CartSerializer(serializers.ModelSerializer):
    cart_items = CartItemSerializer(many=True, read_only=True)
    total_cost = serializers.SerializerMethodField()
    total_quantity = serializers.SerializerMethodField()


    class Meta:
        model = Cart
        fields = ('id', 'user', 'session_key', 'created_at', 'cart_items', 'total_cost', 'total_quantity')
        read_only_fields = fields

    def get_total_cost(self, obj):
        return obj.get_cart_total_cost()

    def get_total_quantity(self, obj):
        return obj.get_cart_total_quantity()