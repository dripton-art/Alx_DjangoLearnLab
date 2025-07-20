from django.urls import path
from .views import list_books
from .views import LibraryDetailView

urlpatterns = [
    path('books/', list_books, name='book_list'),
    path('libraries/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
]
