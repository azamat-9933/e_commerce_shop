from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.shortcuts import get_object_or_404

from cart.models import Cart, CartItem
from store.models import Product
from cart.serializers import CartSerializer, CartItemSerializer
from cart.utils import get_or_create_cart



class CartAPIView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):

        cart = get_or_create_cart(request)

        serializer = CartSerializer(cart)

        return Response(serializer.data, status=status.HTTP_200_OK)


class AddCartItemAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        cart = get_or_create_cart(request)
        product_id = request.data.get('product_id')
        quantity = int(request.data.get('quantity', 1))
        product = get_object_or_404(Product, id=product_id)

        cart_item, created = CartItem.objects.get_or_create(
            cart=cart,
            product=product,
            defaults={'quantity': quantity}
        )

        if not created:
            cart_item.quantity += quantity
            cart_item.save()

        serializer = CartSerializer(cart)
        return Response(serializer.data, status=status.HTTP_201_CREATED)



class RemoveCartItemAPIView(APIView):
    permission_classes = [AllowAny]

    def delete(self, request, item_id):
        cart = get_or_create_cart(request)
        cart_item = get_object_or_404(CartItem, id=item_id, cart=cart)
        cart_item.delete()
        return Response({'success': 'Item Removed'}, status=status.HTTP_204_NO_CONTENT)


class UpdateCartItemQuantityAPIView(APIView):
    permission_classes = [AllowAny]


    def patch(self, request, item_id):
        cart = get_or_create_cart(request)
        cart_item = get_object_or_404(CartItem, id=item_id, cart=cart)

        action = request.data.get('action')

        if action == 'increment':
            cart_item.quantity += 1
        elif action == 'decrement':
            if cart_item.quantity > 1:
                cart_item.quantity -= 1
            else:
                cart_item.delete()
                return Response({'success': 'Cart item deleted !'}, status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({'error': 'Invalid action. Use "increment" or "decrement".'},
                            status=status.HTTP_400_BAD_REQUEST)

        cart_item.save()
        serializer = CartItemSerializer(cart_item)
        return Response(serializer.data, status=status.HTTP_200_OK)
