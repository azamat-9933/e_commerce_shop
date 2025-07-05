from rest_framework import serializers

from store.models import Product


class ProductCategorySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=100)
    slug = serializers.SlugField(max_length=100)
    created_at = serializers.DateTimeField(read_only=True)


class ProductCardSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=100)
    slug = serializers.SlugField(max_length=100)
    created_at = serializers.DateTimeField(read_only=True)
    category = serializers.CharField(max_length=100, source='category.title')
    price = serializers.DecimalField(max_digits=10, decimal_places=2)
    first_image = serializers.SerializerMethodField()

    def get_first_image(self, obj):
        if obj.images.exists():
            return obj.images.first().image.url
        else:
            return None

class CharacteristicFilterSerializer(serializers.Serializer):
    name = serializers.CharField(source='characteristics__name')
    value = serializers.CharField(source='characteristics__value')


class ProductsByMainCategorySerializer(serializers.Serializer):
    children = serializers.SerializerMethodField()
    products = serializers.SerializerMethodField()
    filters = serializers.SerializerMethodField()


    def get_children(self, obj):
        return ProductCategorySerializer(obj.children.all(), many=True).data

    def get_products(self, obj):
        subcategories = obj.children.all()
        products = Product.objects.filter(category__in=subcategories)
        return ProductCardSerializer(products, many=True).data

    def get_filters(self, obj):
        subcategories = obj.children.all()
        products = Product.objects.filter(category__in=subcategories)
        characteristics = products.values('characteristics__name', 'characteristics__value')
        return CharacteristicFilterSerializer(characteristics, many=True).data


class ProductImageSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    image = serializers.ImageField()


class ProductCharacteristicSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100)
    value = serializers.CharField(max_length=100)


class ProductSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=100)
    category = serializers.CharField(max_length=100, source='category.title')
    description = serializers.CharField()
    price = serializers.DecimalField(max_digits=10, decimal_places=2)
    created_at = serializers.DateTimeField(read_only=True)
    stock = serializers.IntegerField()
    slug = serializers.SlugField(max_length=100)
    images = ProductImageSerializer(many=True)
    characteristics = ProductCharacteristicSerializer(many=True)
