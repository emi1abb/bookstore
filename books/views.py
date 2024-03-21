from django.shortcuts import render
from books.models import Book


# Create your views here.
def index(request):
    db_data = Book.objects.all()
    context = {'data': db_data}
    return render(request, 'books/index.html', context)

def book(request, id):
    single_book = Book.objects.get(pk=id)
    context = {'book': single_book}
    return render(request, 'books/book.html', context)