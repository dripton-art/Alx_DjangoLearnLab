from django.urls import path
from .views import (
    CustomBookCreateView,
    CustomBookListView,
    CustomBookDetailView,
    CustomBookUpdateView,
    CustomBookDeleteView
)

urlpatterns = [
    path('books/create', BookCreateView.as_view(), name='book-create'),
    path('books/list', BookListView.as_view(), name='book-list'),
    path('books/list', BookDetailView.as_view(), name='book-detail'),
    path('books/update', BookRetrieveView.as_view(), name='book-retrieve'),
    path('books/delete', BookDestroyView.as_view(), name='book-destroy'),
]