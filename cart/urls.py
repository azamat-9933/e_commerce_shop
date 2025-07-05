from django.urls import path

from cart.views import (
    CartAPIView,
    AddCartItemAPIView,
    RemoveCartItemAPIView,
    UpdateCartItemQuantityAPIView
)

urlpatterns = [
    path('cart/', CartAPIView.as_view(), name='get-cart'),
    path('cart/add/', AddCartItemAPIView.as_view(), name='add-cart-item'),
    path('cart/remove/<int:item_id>/', RemoveCartItemAPIView.as_view(), name='remove-cart-item'),
    path('cart/update/<int:item_id>/', UpdateCartItemQuantityAPIView.as_view(), name='update-cart-item')
]
