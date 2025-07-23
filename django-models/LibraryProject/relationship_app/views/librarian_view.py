from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test

# Helper function to check if user is a Librarian
def is_librarian(user):
    return user.is_authenticated and user.userprofile.role == 'Librarian'

@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_page.html')
