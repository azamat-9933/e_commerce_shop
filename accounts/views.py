from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated

from rest_framework import generics, permissions
from django.shortcuts import get_object_or_404

from accounts.serializers import RegisterSerializer, LoginSerializer
from accounts.serializers import FavoriteProductSerializer, AddFavoriteProductSerializer
from store.models import Product
from accounts.models import FavoriteProduct


class FavoriteListAPIView(generics.ListAPIView):
    serializer_class = FavoriteProductSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return FavoriteProduct.objects.filter(user=user).select_related('product')


class FavoriteAddAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        serializer = AddFavoriteProductSerializer(data=request.data)  # id
        serializer.is_valid(raise_exception=True)

        product = serializer.validated_data['product']  # id
        user = request.user

        if FavoriteProduct.objects.filter(user=user, product=product).exists():
            return Response(
                {"detail": "Product is already in favorites"},
                status=status.HTTP_400_BAD_REQUEST
            )

        favorite_instance = FavoriteProduct.objects.create(user=user, product=product)
        response_serializer = FavoriteProductSerializer(favorite_instance)
        return Response(response_serializer.data, status=status.HTTP_201_CREATED)


class FavoriteRemoveAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def post(self, request, *args, **kwargs):
        user = request.user
        product_identifier = kwargs.get('product_identifier')

        if not product_identifier:
            return Response(
                {"detail": "Product identifier is required"},
                status=status.HTTP_400_BAD_REQUEST
            )
        try:
            product_pk = int(product_identifier)
            product = get_object_or_404(Product, pk=product_pk)
        except ValueError:
            product = get_object_or_404(Product, slug=product_identifier)
        except Product.DoesNotExist:
            return Response(
                {"detail": "Product not found"},
                status=status.HTTP_404_NOT_FOUND
            )
        favorite_instance = get_object_or_404(FavoriteProduct, user=user, product=product)
        favorite_instance.delete()
        return Response(
            {"detail": "Product removed from favorites"},
            status=status.HTTP_204_NO_CONTENT
        )























class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'User registered successfully'},
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            return Response(serializer.validated_data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        request.user.auth_token.delete()
        return Response({'message': 'Logged out successfully'}, status=status.HTTP_200_OK)