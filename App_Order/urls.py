from django.urls import path
from App_Order import views

app_name = 'App_Order'

urlpatterns = [
    path('add/<pk>/' ,views.add_to_cart , name='add'),
    path('cart/' , views.cart_view , name = 'cart'),
    path('remove/<pk>/' , views.remove_form_cart , name='remove'),
    path('increase-item/<pk>/' , views.increase_cart , name='increase'),
    path('deceease-item/<pk>/' , views.decrease_cart , name='decrease'),
]
