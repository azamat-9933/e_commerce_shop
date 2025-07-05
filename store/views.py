from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from store.filters import ProductFilter
from store.models import ProductCategory, Product, ProductImage, ProductCharacteristic
from store.serializers import (ProductCategorySerializer, ProductCardSerializer,
                               ProductSerializer, ProductsByMainCategorySerializer)


class ProductMainCategoryListAPIView(generics.ListAPIView):
    queryset = ProductCategory.objects.filter(parent=None)
    serializer_class = ProductCategorySerializer


class ProductSubCategoryListAPIView(generics.ListAPIView):
    serializer_class = ProductCategorySerializer

    def get_queryset(self):
        main_category_slug = self.kwargs['main_category_slug']
        return ProductCategory.objects.filter(parent__slug=main_category_slug)


class ProductCardListAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductCardSerializer


class ProductCardByCategoryListAPIView(generics.ListAPIView):
    serializer_class = ProductCardSerializer

    def get_queryset(self):
        category_slug = self.kwargs['category_slug']
        return Product.objects.filter(category__slug=category_slug)


class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'slug'
    lookup_url_kwarg = 'product_slug'


class ProductsByMainCategoryAPIView(APIView):
    def get(self, request, slug):
        try:
            category = ProductCategory.objects.get(slug=slug, parent__isnull=True)
        except ProductCategory.DoesNotExist:
            return None

        serializer = ProductsByMainCategorySerializer(category)
        return Response(serializer.data)


class ProductFilterAPIView(generics.ListAPIView):
    serializer_class = ProductCardSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ProductFilter
    

    def get_queryset(self):
        category_slug = self.kwargs['category_slug']
        try:
            category = ProductCategory.objects.get(slug=category_slug)
        except ProductCategory.DoesNotExist:
            return Response({'error': 'Category not found'},status=status.HTTP_404_NOT_FOUND)


        if category.children.exists():
            subcategory_ids = category.children.values_list('id', flat=True)
            return Product.objects.filter(category__in=subcategory_ids)
        else:
            return Product.objects.filter(category=category)