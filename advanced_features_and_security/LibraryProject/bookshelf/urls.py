from django.urls import path
from . import views


urlpatterns = [
    path('', views.list_books, name='list_books'),
    path('create_book', views.create_book, name='create_book'),
    path('edit_book', views.edit_book, name='edit_book'),
    path('delete_book', views.delete_book, name='delete_book'),
]
