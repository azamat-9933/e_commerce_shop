from django.db import models
from django.contrib.auth.models import User

from store.models import Product

# TODO: Model for Cart.

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             null=True, blank=True)
    session_key = models.CharField(max_length=40, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


    def get_cart_total_cost(self):
        return sum(item.get_cost() for item in self.cart_items.all())

    def get_cart_total_quantity(self):
        return sum(item.quantity for item in self.cart_items.all())



    def __str__(self):
        if self.user:
            return str(self.user.username)
        else:
            return str(self.session_key)

    class Meta:
        verbose_name = 'Cart'
        verbose_name_plural = 'Carts'
        ordering = ['-created_at']


# TODO: Model for CartItem.

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='cart_items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.quantity} x {self.product.title}'

    def get_cost(self):
        return self.quantity * self.product.price

    class Meta:
        verbose_name = 'Cart Item'
        verbose_name_plural = 'Cart Items'
        ordering = ['-added_at']


# TODO: create serializers for this models
# TODO: API for getting cart
# TODO: API for add cart items
# TODO: API for remove cart items
# TODO: API for update cart items (add quantity/remove quantity)