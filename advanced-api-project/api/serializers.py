from rest_framework import serializers
from .models import Book, Author
from datetime import date


# BookSerializer — serializes all fields
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
    def validate_publication_year(self, value):
        current_year = date.today().year
        if value > current_year:
            raise serializers.ValidationError('Publication year cannot be in the future.')
        return value

class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)  # Nested BookSerializer to serialize the related books dynamically.

     class Meta:
        model = Author
        fields = ['name', 'books'] # only show name and nested books
