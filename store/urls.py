from django.urls import path

from store.views import (ProductMainCategoryListAPIView, ProductSubCategoryListAPIView, ProductCardListAPIView,
                         ProductCardByCategoryListAPIView, ProductDetailAPIView, ProductsByMainCategoryAPIView,
                         ProductFilterAPIView)

urlpatterns = [
    # TODO: API для показа всех категории (основных категорий)
    path('main/categories/', ProductMainCategoryListAPIView.as_view(), name='main-categories'),

    # TODO: API для показа всех подкатегории (category_slug)
    path('sub/categories/<slug:main_category_slug>/', ProductSubCategoryListAPIView.as_view(),
         name='sub-categories'),

    # TODO: API для показа всех подкатегории и продуктов при нажатии на основную категорию
    path('products/by/main/category/<slug:slug>/',
         ProductsByMainCategoryAPIView.as_view(),
         name='products-by-main-category'),

    # TODO: Показ всех продуктов
    path('products/', ProductCardListAPIView.as_view(), name='products'),
    # TODO: Показ всех продуктов по подкатегории

    path('products/by/category/<slug:category_slug>/', ProductCardByCategoryListAPIView.as_view(),
         name='products-by-category'),

    # TODO: Показ product detail
    path('product/detail/<slug:product_slug>/', ProductDetailAPIView.as_view(), name='product-detail'),

    # # TODO: Product Filter (цена, тэг, категория, подкатегория)
    path('products/filter/<slug:category_slug>/',
         ProductFilterAPIView.as_view(),
         name='product-filter')
]