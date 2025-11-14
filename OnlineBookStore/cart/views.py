from django.shortcuts import render


def view_cart(request):
    cart_items = [
        {
            "title": "Harry Potter",
            "author": "J.K. Rowling",
            "price": 499,
            "description": "A magical story of friendship and adventure.",
            "image": "https://m.media-amazon.com/images/I/81iqZ2HHD-L.jpg",
        },
        {
            "title": "The Alchemist",
            "author": "Paulo Coelho",
            "price": 299,
            "description": "A shepherd travels the world in search of his destiny.",
            "image": "https://m.media-amazon.com/images/I/71aFt4+OTOL.jpg",
        },
    ]

    total_price = sum(item["price"] for item in cart_items)

    return render(
        request,
        "add_to_cart.html",
        {"cart_items": cart_items, "total_price": total_price},
    )


def buy_now(request):
    book = {
        "title": "Atomic Habits",
        "author": "James Clear",
        "price": 450,
        "description": "A practical guide to building good habits and breaking bad ones.",
        "image": "https://m.media-amazon.com/images/I/91bYsX41DVL.jpg",
    }
    return render(request, "buy_now.html", {"book": book})
