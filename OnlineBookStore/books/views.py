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
        {
            "title": "The Great Gatsby",
            "author": "F. Scott Fitzgerald",
            "price": 350,
            "description": "A tragic love story set in the roaring twenties.",
            "image": "https://m.media-amazon.com/images/I/81af+MCATTL.jpg",
        },
        {
            "title": "1984",
            "author": "George Orwell",
            "price": 320,
            "description": "A chilling dystopian tale of surveillance and control.",
            "image": "https://m.media-amazon.com/images/I/71kxa1-0mfL.jpg",
        },
        {
            "title": "To Kill a Mockingbird",
            "author": "Harper Lee",
            "price": 399,
            "description": "A powerful story of justice and racial inequality.",
            "image": "/static/images/mocking.jpeg",
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
        {
            "title": "Sapiens",
            "author": "Yuval Noah Harari",
            "price": 499,
            "description": "The story of humankind, from evolution to modern society.",
            "image": "https://m.media-amazon.com/images/I/713jIoMO3UL.jpg",
        },
        {
            "title": "The Elegant Universe",
            "author": "Brian Greene",
            "price": 420,
            "description": "A deep dive into string theory and the fabric of the universe.",
            "image": "https://m.media-amazon.com/images/I/81p2Tj9uEwL.jpg",
        },
        {
            "title": "Cosmos",
            "author": "Carl Sagan",
            "price": 450,
            "description": "A breathtaking journey through space, science, and humanity.",
            "image": "https://m.media-amazon.com/images/I/91w3Vjv1edL.jpg",
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
        {
            "title": "Think and Grow Rich",
            "author": "Napoleon Hill",
            "price": 299,
            "description": "A classic guide to developing a mindset for success.",
            "image": "https://m.media-amazon.com/images/I/81s0B6NYXML.jpg",
        },
        {
            "title": "You Are a Badass",
            "author": "Jen Sincero",
            "price": 350,
            "description": "Learn to create a life you love with confidence and mindset shifts.",
            "image": "https://m.media-amazon.com/images/I/81M8NsXRQ-L.jpg",
        },
        {
            "title": "How to Win Friends & Influence People",
            "author": "Dale Carnegie",
            "price": 399,
            "description": "A must-read guide to improving communication and relationships.",
            "image": "https://m.media-amazon.com/images/I/81WojUxbbFL.jpg",
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
        {
            "title": "The Gruffalo",
            "author": "Julia Donaldson",
            "price": 280,
            "description": "A clever mouse outsmarts a monster in the woods.",
            "image": "https://m.media-amazon.com/images/I/91pR9wKJolL.jpg",
        },
        {
            "title": "Diary of a Wimpy Kid",
            "author": "Jeff Kinney",
            "price": 350,
            "description": "A hilarious journey through school and life.",
            "image": "https://m.media-amazon.com/images/I/81tZf7AbBuL.jpg",
        },
        {
            "title": "The Cat in the Hat",
            "author": "Dr. Seuss",
            "price": 260,
            "description": "A fun, rhyming classic loved by children worldwide.",
            "image": "https://m.media-amazon.com/images/I/71xZ8M9RUpL.jpg",
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
