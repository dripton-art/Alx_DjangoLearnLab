from django.shortcuts import render
from .serializers import BookSerializer
from rest_framework import generics
from rest_framework import viewsets
from .models import Book

# Create your views here.
class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


#This viewset will handle all CRUD operations
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    