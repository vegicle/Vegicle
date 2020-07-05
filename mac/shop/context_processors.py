from cart.models import Item
from cart.cart import Cart


def cart(request):
    items_count = 0
    for item in Cart(request):
        items_count = items_count + 1
    return {'cart_items': items_count}
