from django.shortcuts import render, redirect, get_object_or_404
from .models import Book
from django.views.generic.detail import DetailView
from .models import Library
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators import permission_required

# Create your views here.
def list_books(request):
      """Retrieves all books and renders a template displaying the list."""
      books = Book.objects.all()
      context = {'list_books': books}
      return render(request, 'relationship_app/list_books.html', context)

@permission_required('relationship_app.can_add_book')
def add_book(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        if title and author:
            Book.objects.create(title=title, author=author)
            return redirect('list_books')
        else:
            error = "Both title and author are required."
            return render(request, 'relationship_app/add_book.html', {'error': error})
    return render(request, 'relationship_app/add_book.html')
 


@permission_required('relationship_app.can_change_book')
def change_book(request, book_id):
     book = get_object_or_404(Book, id=book_id)
    
    if request.method == 'POST':
        book.title = request.POST.get('title')
        book.author = request.POST.get('author')
        book.save()
        return redirect('list_books')
    else:
        error = "Both title and author are required."
        return render(request, 'relationship_app/add_book.html', {'error': error})
    return render(request, 'relationship_app/edit_book.html', {'book': book})


@permission_required('relationship_app.can_delete_book')
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    
    if request.method == 'POST':
        book.delete()
        return redirect('list_books')
    return render(request, 'relationship_app/delete.html', {'book': book})


class LibraryDetailView(DetailView):
    """A class-based view for displaying details of a specific book."""  
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = self.object.book.all()
        return context

def register(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login')  # After registration, go to login
    return render(request, 'relationship_app/register.html', {'form': form})

def is_member(user):
    return user.is_authenticated and not user.is_staff and not user.is_superuser

def is_librarian(user):
    return user.groups.filter(name='Librarian').exists()

def is_admin(user):
    return user.is_superuser

@user_passes_test(is_member)
def member_view(request):
    return render(request, "relationship_app/member_view.html")

@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, "relationship_app/librarian_view.html")

@user_passes_test(is_admin)
def admin_view(request):
    return render(request, "relationship_app/admin_view.html")
