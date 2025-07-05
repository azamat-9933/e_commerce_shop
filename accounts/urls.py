from django.urls import path

from accounts.views import (RegisterView, LoginView, LogoutView,
                            FavoriteListAPIView, FavoriteAddAPIView,
                            FavoriteRemoveAPIView)

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),


    path('favorites/', FavoriteListAPIView.as_view(), name='favorites'),
    path('favorites/add/', FavoriteAddAPIView.as_view(), name='favorite_add'),
    path('favorites/remove/<str:product_identifier>/',
         FavoriteRemoveAPIView.as_view(), name='favorite_remove'),
]
