from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def admin_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        # Authenticate using Django's user system
        user = authenticate(request, username=username, password=password)

        if user is not None and user.is_staff:
            login(request, user)
            return redirect("/admin-panel/")
        else:
            messages.error(request, "Invalid credentials or not an admin.")

    return render(request, "admin_panel/login.html")


def admin_logout(request):
    logout(request)
    return redirect("/admin-panel/login/")


def admin_required(view_func):
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated or not request.user.is_staff:
            return redirect("/admin-panel/login/")
        return view_func(request, *args, **kwargs)

    return wrapper


USERS = [
    {
        "id": 1,
        "username": "HitOza",
        "email": "hit@example.com",
        "orders": 5,
        "status": "Active",
    },
    {
        "id": 2,
        "username": "John",
        "email": "john@example.com",
        "orders": 2,
        "status": "Active",
    },
]

BOOKS = [
    {
        "id": 1,
        "title": "Harry Potter",
        "author": "J.K. Rowling",
        "price": 499,
        "stock": 12,
        "image": "https://m.media-amazon.com/images/I/81iqZ2HHD-L.jpg",
    },
    {
        "id": 2,
        "title": "Atomic Habits",
        "author": "James Clear",
        "price": 450,
        "stock": 5,
        "image": "https://m.media-amazon.com/images/I/91bYsX41DVL.jpg",
    },
]

CATEGORIES = [
    {"id": 1, "name": "Fiction"},
    {"id": 2, "name": "Science"},
    {"id": 3, "name": "Self Help"},
]

ORDERS = [
    {"id": 101, "user": "HitOza", "items": 3, "total": 1299, "status": "Pending"},
    {"id": 102, "user": "John", "items": 1, "total": 499, "status": "Delivered"},
]

ADDRESSES = [
    {
        "id": 1,
        "user": "HitOza",
        "address": "21 MG Road",
        "city": "Mumbai",
        "pincode": "400001",
    },
]

OFFERS = [
    {"id": 1, "code": "FIRST50", "discount": 50, "expiry": "2025-12-31"},
]


@admin_required
def dashboard(request):
    data = {
        "total_users": len(USERS),
        "total_orders": len(ORDERS),
        "total_books": len(BOOKS),
        "revenue": 45000,
    }
    return render(request, "admin_panel/dashboard.html", data)


@admin_required
def admin_users(request):
    return render(request, "admin_panel/users.html", {"users": USERS})


@admin_required
def admin_books(request):
    return render(request, "admin_panel/books.html", {"books": BOOKS})


@admin_required
def admin_categories(request):
    return render(request, "admin_panel/categories.html", {"categories": CATEGORIES})


@admin_required
def admin_orders(request):
    return render(request, "admin_panel/orders.html", {"orders": ORDERS})


@admin_required
def admin_addresses(request):
    return render(request, "admin_panel/addresses.html", {"addresses": ADDRESSES})


@admin_required
def admin_offers(request):
    return render(request, "admin_panel/offers.html", {"offers": OFFERS})
