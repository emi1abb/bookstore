from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='books.urls'),
    path('book/<int:id>', views.book, name='book.url')
]