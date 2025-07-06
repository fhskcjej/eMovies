# cart/urls.py
from django.urls import path
from . import views

app_name = "cart"

urlpatterns = [
    path("add/<int:movie_id>/", views.add_to_cart, name="add_to_cart"),
    path("remove/<int:movie_id>/", views.remove_from_cart, name="remove_from_cart"),
    path("clear/", views.clear_cart, name="clear_cart"),
    path('cart/', views.view_cart, name='cart'),
    path('checkout', views.checkout, name='checkout')
]