from django.urls import path
from .views import list_books
from .views import LibraryDetailView
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from relationship_app.views.admin_view import admin_view
from relationship_app.views.librarian_view import librarian_view
from relationship_app.views.member_view import member_view


urlpatterns = [
    path('books/', list_books, name='book_list'),
    path('libraries/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    
    path('register/', views.register, name='register'),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),

    path('admin/', admin_view.admin_view, name='admin_view'),
    path('librarian/', librarian_view.librarian_view, name='librarian_view'),
    path('member/', member_view.member_view, name='member_view'),
]
