import json
from django.shortcuts import render


books_data = open('books/books.json').read()
data = json.loads(books_data)

# Create your views here.
def index(request):
    context = {'data': data}
    return render(request, 'books/index.html', context)

def book(request, id):
    single_book = list()
    for book in data:
        if book['id'] == id:
            single_book = book
    
    context = {'book': single_book}
    return render(request, 'books/book.html', context)