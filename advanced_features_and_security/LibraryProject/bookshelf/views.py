from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import permission_required
from .models import Book

# Create your views here.

# Only users with 'bookshelf.can_view' can access this page
@permission_required('bookshelf.can_delete_book', raise_exception=True)
def list_books(request):
      """Retrieves all books and renders a template displaying the list."""
      books = Book.objects.all()
      context = {'list_books': books}
      return render(request, 'bookshelf/list_books.html', context)

# Only users with 'bookshelf.can_create' permission can add books
@permission_required('bookshelf.can_create_book', raise_exception=True)
def create_book(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        if title and author:
            Book.objects.create(title=title, author=author)
            return redirect('list_books')
        else:
            error = "Both title and author are required."
            return render(request, 'bookshelf/create_book.html', {'error': error})
    return render(request, 'bookshelf/create_book.html')

# Only users with 'bookshelf.can_edit' can edit books
@permission_required('bookshelf.can_edit_book', raise_exception=True)
def edit_book(request, book_id):
     book = get_object_or_404(Book, id=book_id)

     if request.method == 'POST':
        book.title = request.POST.get('title')
        book.author = request.POST.get('author')
        book.save()
        return redirect('list_books')
     else:
        error = "Both title and author are required."
        return render(request, 'bookshelf/create_book.html', {'error': error})
     return render(request, 'bookshelf/edit_book.html', {'book': book})

# Only users with 'bookshelf.can_delete' can delete books
@permission_required('bookshelf.can_delete_book', raise_exception=True)
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)

    if request.method == 'POST':
        book.delete()
        return redirect('list_books')
    return render(request, 'bookshelf/delete.html', {'book': book})
