from django.urls import path
from . import views

app_name = "cart"

urlpatterns = [
    path("", views.view_cart, name="view_cart"),
    path("buy_now/", views.buy_now, name="buy_now"),
]
