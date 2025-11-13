from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('categories/', views.categories, name='categories'),
    path('fiction/', views.fiction_books, name='fiction_books'),
    path('science/', views.science_books, name='science_books'),
    path('self-help/', views.self_help_books, name='self_help_books'),
    path('children/', views.children_books, name='children_books'),
]
