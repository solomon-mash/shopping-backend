from rest_framework import serializers

from .models import Product, Shop, Cart, CartItem


class ProductSerializer(serializers.ModelSerializer):
    shop_name = serializers.SerializerMethodField()
    class Meta:
        model = Product
        fields = ['product_id', 'name', 'description', 'image', 'price', 'category', 'shop', 'shop_name']

    def get_shop_name(self, obj):
        return obj.shop.name  # Retrieve the shop name


class CartItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    id = serializers.IntegerField()

    class Meta:
        model = CartItem
        fields = ['id', 'product', 'quantity', 'total_price']

class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True, read_only=True)

    class Meta:
        model = Cart
        fields = ['user', 'items']
