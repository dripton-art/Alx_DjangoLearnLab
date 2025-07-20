from django.shortcuts import render
from .models import Book
from django.views.generic.detail import DetailView
from .models import Library

# Create your views here.
def book_list(request):
      """Retrieves all books and renders a template displaying the list."""
      books = Book.objects.all()
      context = {'book_list': books}
      return render(request, 'books/book_list.html', context)

class LibraryDetailView(DetailView):
    """A class-based view for displaying details of a specific book."""  
    model = Library
    template_name = 'libraries/library_detail.html'
    context_object_name = 'library'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = self.object.book.all()
        return context
