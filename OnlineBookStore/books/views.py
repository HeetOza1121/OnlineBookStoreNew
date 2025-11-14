from django.shortcuts import render

BOOKS_DATA = {
    "fiction": [
        {
            "title": "Harry Potter",
            "author": "J.K. Rowling",
            "price": 499,
            "description": "A magical story of friendship and adventure in the wizarding world.",
            "image": "/static/images/harrypotter.jpeg",
        },
        {
            "title": "The Alchemist",
            "author": "Paulo Coelho",
            "price": 299,
            "description": "A shepherd travels the world in search of his destiny.",
            "image": "/static/images/alcemist.jpeg",
        },
        {
            "title": "The Great Gatsby",
            "author": "F. Scott Fitzgerald",
            "price": 350,
            "description": "A tragic love story set in the roaring twenties.",
            "image": "/static/images/greatgatsby.jpeg",
        },
        {
            "title": "1984",
            "author": "George Orwell",
            "price": 320,
            "description": "A chilling dystopian tale of surveillance and control.",
            "image": "/static/images/1984.jpeg",
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
            "image": "/static/images/bhot.jpeg",
        },
        {
            "title": "The Selfish Gene",
            "author": "Richard Dawkins",
            "price": 450,
            "description": "Evolution through the lens of genetics and behavior.",
            "image": "/static/images/selfishgene.jpeg",
        },
        {
            "title": "Sapiens",
            "author": "Yuval Noah Harari",
            "price": 499,
            "description": "The story of humankind, from evolution to modern society.",
            "image": "/static/images/sapeins.jpeg",
        },
        {
            "title": "The Elegant Universe",
            "author": "Brian Greene",
            "price": 420,
            "description": "A deep dive into string theory and the fabric of the universe.",
            "image": "/static/images/elegantuni.jpeg",
        },
        {
            "title": "Cosmos",
            "author": "Carl Sagan",
            "price": 450,
            "description": "A breathtaking journey through space, science, and humanity.",
            "image": "/static/images/cosmos.jpeg",
        },
    ],
    "self_help": [
        {
            "title": "Atomic Habits",
            "author": "James Clear",
            "price": 450,
            "description": "Learn to build better habits and improve daily life.",
            "image": "/static/images/atomic.jpeg",
        },
        {
            "title": "The 7 Habits of Highly Effective People",
            "author": "Stephen Covey",
            "price": 499,
            "description": "Timeless lessons for success and leadership.",
            "image": "/static/images/sevenhabits.jpeg",
        },
        {
            "title": "Think and Grow Rich",
            "author": "Napoleon Hill",
            "price": 299,
            "description": "A classic guide to developing a mindset for success.",
            "image": "/static/images/thinkngrow.jpeg",
        },
        {
            "title": "You Are a Badass",
            "author": "Jen Sincero",
            "price": 350,
            "description": "Learn to create a life you love with confidence and mindset shifts.",
            "image": "/static/images/badass.jpeg",
        },
        {
            "title": "How to Win Friends & Influence People",
            "author": "Dale Carnegie",
            "price": 399,
            "description": "A must-read guide to improving communication and relationships.",
            "image": "/static/images/friendsandpeople.jpeg",
        },
    ],
    "children": [
        {
            "title": "Matilda",
            "author": "Roald Dahl",
            "price": 299,
            "description": "A brilliant girl with extraordinary powers.",
            "image": "/static/images/matilda.jpeg",
        },
        {
            "title": "Charlotte's Web",
            "author": "E.B. White",
            "price": 350,
            "description": "A heartwarming story of friendship between a pig and a spider.",
            "image": "/static/images/charlotte.jpeg",
        },
        {
            "title": "The Gruffalo",
            "author": "Julia Donaldson",
            "price": 280,
            "description": "A clever mouse outsmarts a monster in the woods.",
            "image": "/static/images/gruffalo.jpeg",
        },
        {
            "title": "Diary of a Wimpy Kid",
            "author": "Jeff Kinney",
            "price": 350,
            "description": "A hilarious journey through school and life.",
            "image": "/static/images/winkykid.jpeg",
        },
        {
            "title": "The Cat in the Hat",
            "author": "Dr. Seuss",
            "price": 260,
            "description": "A fun, rhyming classic loved by children worldwide.",
            "image": "/static/images/catinhat.jpeg",
        },
    ],
}


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
            "cover_image": "/static/images/atomic.jpeg",
        },
        {
            "title": "Harry Potter",
            "author": "J.K. Rowling",
            "price": 499,
            "cover_image": "/static/images/harrypotter.jpeg",
        },
        {
            "title": "The Alchemist",
            "author": "Paulo Coelho",
            "price": 299,
            "cover_image": "/static/images/alcemist.jpeg",
        },
        {
            "title": "A Brief History of Time",
            "author": "Stephen Hawking",
            "price": 399,
            "cover_image": "/static/images/bhot.jpeg",
        },
    ]

    return render(
        request, "home.html", {"categories": categories, "bestsellers": bestsellers}
    )


def categories(request):
    categories = ["Fiction", "Science", "Self Help", "Children"]
    return render(request, "categories.html", {"categories": categories})


def fiction_books(request):
    return render(request, "fiction.html", {"books": BOOKS_DATA["fiction"]})


def science_books(request):
    return render(request, "science.html", {"books": BOOKS_DATA["science"]})


def self_help_books(request):
    return render(request, "self_help.html", {"books": BOOKS_DATA["self_help"]})


def children_books(request):
    return render(request, "children.html", {"books": BOOKS_DATA["children"]})
