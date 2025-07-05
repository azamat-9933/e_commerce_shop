from cart.models import Cart


def get_or_create_cart(request):
    cart = None

    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user)
    else:
        session_key = request.session.session_key
        if not session_key:
            request.session.save()

        cart, created = Cart.objects.get_or_create(session_key=session_key, user=None)

    return cart