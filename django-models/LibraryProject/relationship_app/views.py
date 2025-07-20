from django.shortcuts import render
from .models import Book

# Create your views here.
def book_list(request):
      """Retrieves all books and renders a template displaying the list."""
      books = Book.objects.all()
      context = {'book_list': books}
      return render(request, 'books/book_list.html', context)
