from django.urls import path

from blog.views import PostCategoryListAPIView, PostListAPIView, PostsByCategoryAPIView, PostDetailAPIView

urlpatterns = [
    path('categories/', PostCategoryListAPIView.as_view(), name='categories'),
    path('posts/', PostListAPIView.as_view(), name='posts'),
    path('posts/by/category/<str:category_slug>/',
         PostsByCategoryAPIView.as_view(),
         name='posts_by_category'),
    path('post/detail/<str:post_slug>/',
         PostDetailAPIView.as_view(), name='post_detail'),

]