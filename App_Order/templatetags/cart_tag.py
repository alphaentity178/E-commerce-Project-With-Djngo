from django import template
from App_Order.models import Order

register = template.Library()

@register.filter
def get_total(user):
    # print(f"User: {user}") 
    order = Order.objects.filter(user = user , ordered=False)
    if order.exists():
        return order[0].orderitems.count()
    else :
        return 0
    