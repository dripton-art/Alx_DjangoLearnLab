from django.urls import path, include
from .views import BookList, BookViewSet
from . import views
from rest_framework.routers import DefaultRouter

#Place router here
router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='books_all')  # This handles full CRUD via /books/

urlpatterns = [
    # Route for the BookList view (ListAPIView)
    path('books/', BookList.as_view(), name='book-list'),

    # Include the router URLs for BookViewSet (all CRUD operations)
    path('', include(router.urls)),
]