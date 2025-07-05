from django.contrib import admin

from store.models import Product, ProductCategory, ProductImage, ProductCharacteristic


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1
    fk_name = 'product'


class ProductCharacteristicInline(admin.TabularInline):
    model = ProductCharacteristic
    extra = 1
    fk_name = 'product'


@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug', 'created_at', 'parent')
    list_display_links = ('title',)
    search_fields = ('title', 'slug')
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('created_at',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'stock', 'created_at', 'category')
    list_display_links = ('title',)
    search_fields = ('title', 'slug')
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('created_at', 'category')
    inlines = [ProductImageInline, ProductCharacteristicInline]


@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'image')
    list_display_links = ('product',)


@admin.register(ProductCharacteristic)
class ProductCharacteristicAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'name', 'value')
    list_display_links = ('product',)
