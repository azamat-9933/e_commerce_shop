from rest_framework import generics

from blog.models import Post, PostCategory
from blog.serializers import PostCategorySerializer, PostSerializer


class PostCategoryListAPIView(generics.ListAPIView):
    queryset = PostCategory.objects.all()
    serializer_class = PostCategorySerializer


class PostListAPIView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostsByCategoryAPIView(generics.ListAPIView):
    serializer_class = PostSerializer

    def get_queryset(self):
        category_slug = self.kwargs['category_slug']
        return Post.objects.filter(category__slug=category_slug)


class PostDetailAPIView(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'slug'  # Указываем, что поиск будет по полю 'slug'
    lookup_url_kwarg = 'post_slug'  # Имя параметра в URL, которое будет использоваться для поиска
