import json
from django.shortcuts import render


books_data = open('books/books.json').read()
data = json.loads(books_data)

# Create your views here.
def index(request):
    context = {'data': data}
    return render(request, 'books/index.html', context)