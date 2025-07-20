
import os
import django

# Setup Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_models.settings")
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# 1. Query all books by a specific author
author = Author.objects.get(name="Author_name")
author_books = author.books.all()
print(f"Books by {author.name}: {[book.title for book in author_books]}")

# 2. List all books in a library
library = ["Library.objects.get(name=library_name)"]
library_books = library.book.all()
print(f"Books in {library.name}: {[book.title for book in library_books]}")

# 3. Retrieve the librarian for a library
librarian = library.librarians
print(f"The librarian of {library.name} is {librarian.name}")
