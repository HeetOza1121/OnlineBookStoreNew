from django.urls import path
from . import views

urlpatterns = [
    path("", views.dashboard, name="admin_dashboard"),
    path("login/", views.admin_login, name="admin_login"),
    path("logout/", views.admin_logout, name="admin_logout"),
    path("users/", views.admin_users, name="admin_users"),
    path("books/", views.admin_books, name="admin_books"),
    path("categories/", views.admin_categories, name="admin_categories"),
    path("orders/", views.admin_orders, name="admin_orders"),
    path("addresses/", views.admin_addresses, name="admin_addresses"),
    path("offers/", views.admin_offers, name="admin_offers"),
]
