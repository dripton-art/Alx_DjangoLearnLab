from django.urls import path
from . import views
from django.contrib.auth import views as auth_views



urlpatterns = [
    path('', views.list_books, name='list_books'),
    path('login/', auth_views.LoginView.as_view(template_name='bookshelf/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='bookshelf/logout.html'), name='logout'),
    path('create_book', views.create_book, name='create_book'),
    path('edit_book', views.edit_book, name='edit_book'),
    path('delete_book', views.delete_book, name='delete_book'),
]
