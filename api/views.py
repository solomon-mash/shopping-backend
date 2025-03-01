from rest_framework.views import APIView
from .models import Products
from .serializers import ProductSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework import status
from .models import Product, CartItem, Cart
from .serializers import ProductSerializer, CartSerializer, CartItemSerializer
# Create your views here.

class ProductList(APIView):
    def get(self, request):
        data = Products.objects.all()
        serializer = ProductSerializer(data, many=True)
        return Response(serializer.data)
      


@api_view(['GET'])
def get_cart(request, user_id):
    try:
        cart = Cart.objects.get(user_id=user_id)
        serializer = CartSerializer(cart)
        return Response(serializer.data)
    except Cart.DoesNotExist:
        return Response({'message': 'Cart not found'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def add_to_cart(request, user_id):
    product_id = request.data.get('product_id')
    quantity = int(request.data.get('quantity', 1))

    user = User.objects.get(id=user_id)
    cart, created = Cart.objects.get_or_create(user=user)
    
    product = Product.objects.get(product_id=product_id)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    
    if not created:
        cart_item.quantity += quantity
    cart_item.save()

    return Response({'message': 'Added to cart'}, status=status.HTTP_200_OK)


@api_view(['DELETE'])
def remove_from_cart(request, cart_item_id):
    try:
        cart_item = CartItem.objects.get(id=cart_item_id)
        cart_item.delete()
        return Response({'message': 'Removed from cart'}, status=status.HTTP_204_NO_CONTENT)
    except CartItem.DoesNotExist:
        return Response({'message': 'Item not found'}, status=status.HTTP_404_NOT_FOUND)
