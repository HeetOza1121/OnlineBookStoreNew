from django.shortcuts import render

BOOKS_DATA = {
    "fiction": [
        {
            "title": "Harry Potter",
            "author": "J.K. Rowling",
            "price": 499,
            "description": "A magical story of friendship and adventure in the wizarding world.",
            "image": "https://m.media-amazon.com/images/I/81iqZ2HHD-L.jpg",
        },
        {
            "title": "The Alchemist",
            "author": "Paulo Coelho",
            "price": 299,
            "description": "A shepherd travels the world in search of his destiny.",
            "image": "https://m.media-amazon.com/images/I/71aFt4+OTOL.jpg",
        },
    ],
    "science": [
        {
            "title": "A Brief History of Time",
            "author": "Stephen Hawking",
            "price": 399,
            "description": "Explore the mysteries of space, time, and black holes.",
            "image": "https://m.media-amazon.com/images/I/81t2CVWEsUL.jpg",
        },
        {
            "title": "The Selfish Gene",
            "author": "Richard Dawkins",
            "price": 450,
            "description": "Evolution through the lens of genetics and behavior.",
            "image": "https://m.media-amazon.com/images/I/81yE3UxD2HL.jpg",
        },
    ],
    "self_help": [
        {
            "title": "Atomic Habits",
            "author": "James Clear",
            "price": 450,
            "description": "Learn to build better habits and improve daily life.",
            "image": "https://m.media-amazon.com/images/I/91bYsX41DVL.jpg",
        },
        {
            "title": "The 7 Habits of Highly Effective People",
            "author": "Stephen Covey",
            "price": 499,
            "description": "Timeless lessons for success and leadership.",
            "image": "https://m.media-amazon.com/images/I/81bGKUa1e0L.jpg",
        },
    ],
    "children": [
        {
            "title": "Matilda",
            "author": "Roald Dahl",
            "price": 299,
            "description": "A brilliant girl with extraordinary powers.",
            "image": "https://m.media-amazon.com/images/I/81c4jY5vJcL.jpg",
        },
        {
            "title": "Charlotte's Web",
            "author": "E.B. White",
            "price": 350,
            "description": "A heartwarming story of friendship between a pig and a spider.",
            "image": "https://m.media-amazon.com/images/I/81k2Gmal+VL.jpg",
        },
    ],
}

# 🏠 Home Page
def home(request):
    categories = [
        {"name": "Fiction", "url": "/books/fiction/"},
        {"name": "Science", "url": "/books/science/"},
        {"name": "Self Help", "url": "/books/self-help/"},
        {"name": "Children", "url": "/books/children/"},
    ]

    bestsellers = [
        {
            "title": "Atomic Habits",
            "author": "James Clear",
            "price": 450,
            "cover_image": "https://m.media-amazon.com/images/I/91bYsX41DVL.jpg",
        },
        {
            "title": "Harry Potter",
            "author": "J.K. Rowling",
            "price": 499,
            "cover_image": "https://m.media-amazon.com/images/I/81iqZ2HHD-L.jpg",
        },
        {
            "title": "The Alchemist",
            "author": "Paulo Coelho",
            "price": 299,
            "cover_image": "https://m.media-amazon.com/images/I/71aFt4+OTOL.jpg",
        },
        {
            "title": "A Brief History of Time",
            "author": "Stephen Hawking",
            "price": 399,
            "cover_image": "https://m.media-amazon.com/images/I/81t2CVWEsUL.jpg",
        },
    ]

    return render(request, "home.html", {"categories": categories, "bestsellers": bestsellers})

# 📚 Categories Page
def categories(request):
    categories = ["Fiction", "Science", "Self Help", "Children"]
    return render(request, "categories.html", {"categories": categories})

# 🔖 Category-wise Book Pages
def fiction_books(request):
    return render(request, "fiction.html", {"books": BOOKS_DATA["fiction"]})

def science_books(request):
    return render(request, "science.html", {"books": BOOKS_DATA["science"]})

def self_help_books(request):
    return render(request, "self_help.html", {"books": BOOKS_DATA["self_help"]})

def children_books(request):
    return render(request, "children.html", {"books": BOOKS_DATA["children"]})
