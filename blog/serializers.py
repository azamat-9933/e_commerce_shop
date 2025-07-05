from rest_framework import serializers

from blog.models import Post, PostCategory


class PostCategorySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=100)
    slug = serializers.SlugField(max_length=100)
    created_at = serializers.DateTimeField(read_only=True)


class PostSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=100)
    slug = serializers.SlugField(max_length=100)
    content = serializers.CharField()
    created_at = serializers.DateTimeField(read_only=True)
    image = serializers.ImageField()
    category = PostCategorySerializer()
