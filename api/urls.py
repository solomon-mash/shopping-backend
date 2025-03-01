from django.urls import path
from .views import ProductList, get_cart, add_to_cart, remove_from_cart



urlpatterns = [
    path('products/', ProductList.as_view(), name="ProductList"),
    path('cart/<int:user_id>/', get_cart, name='get_cart'),
    path('cart/<int:user_id>/add/', add_to_cart, name='add_to_cart'),
    path('cart/item/<int:cart_item_id>/remove/', remove_from_cart, name='remove_from_cart'),

]