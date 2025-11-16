from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("admin-panel/", include("Admin_Panel.urls")),
    path("", include("books.urls")),
    path("books/", include("books.urls")),
    path("cart/", include("cart.urls")),
    path("users/", include("users.urls")),
    path("orders/", include("orders.urls")),
]
