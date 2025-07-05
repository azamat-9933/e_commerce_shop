from django.contrib import admin

from accounts.models import FavoriteProduct


@admin.register(FavoriteProduct)
class FavoriteProductAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'added_at')
    list_display_links = ('product',)
    list_filter = ('added_at',)
    search_fields = ('user', 'product')


