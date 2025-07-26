# CREATE
from bookshelf.models import Book
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
# Output: <Book: 1984>

# RETRIEVE
book = Book.objects.get(title="1984")
print(book.title, book.author, book.publication_year)
# Output: 1984 George Orwell 1949

# UPDATE
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()
print(book.title)
# Output: Nineteen Eighty-Four

# DELETE
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()

# Output: <QuerySet []>
