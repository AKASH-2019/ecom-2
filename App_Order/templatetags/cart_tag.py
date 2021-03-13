from django import template
from App_Order.models import Order, Cart

register = template.Library()


@register.filter
def cart_total(user):
    order = Order.objects.filter(user=user, ordered=False)

    if order.exists():
        return order[0].orderitems.count()
    else:
        return 0
    # # # another way
    # cart = Cart.objects.filter(user=user, purchased=False)
    #
    # if cart.exists():
    #     return cart.count()
    # else:
    #     return 0