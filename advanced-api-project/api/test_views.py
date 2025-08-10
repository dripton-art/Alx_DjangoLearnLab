from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from .models import Book

class BookAPITestCase(APITestCase):

    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username="testuser", password="password123")

        # Create sample books
        self.book1 = Book.objects.create(
            title="Book One",
            author="Author A",
            publication_year=2020
        )
        self.book2 = Book.objects.create(
            title="Book Two",
            author="Author B",
            publication_year=2021
        )

        self.list_url = reverse("book-list")  # Adjust if your URL name differs

    def test_list_books_unauthenticated(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_create_book_authenticated(self):
        self.client.login(username="testuser", password="password123")
        data = {
            "title": "New Book",
            "author": "New Author",
            "publication_year": 2022
        }
        response = self.client.post(self.list_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)

    def test_create_book_unauthenticated(self):
        data = {
            "title": "Fail Book",
            "author": "Nobody",
            "publication_year": 2023
        }
        response = self.client.post(self.list_url, data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_update_book_authenticated(self):
        self.client.login(username="testuser", password="password123")
        url = reverse("book-detail", kwargs={"pk": self.book1.pk})
        data = {
            "title": "Updated Book",
            "author": "Updated Author",
            "publication_year": 2025
        }
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, "Updated Book")

    def test_delete_book_authenticated(self):
        self.client.login(username="testuser", password="password123")
        url = reverse("book-detail", kwargs={"pk": self.book1.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)

    def test_filter_books_by_title(self):
        response = self.client.get(self.list_url, {"title": "Book One"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["title"], "Book One")

    def test_search_books(self):
        # Search functionality if implemented
        response = self.client.get(self.list_url, {"search": "Author A"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(any("Author A" in book["author"] for book in response.data))

    def test_order_books_by_year(self):
        response = self.client.get(self.list_url, {"ordering": "-publication_year"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(
            response.data[0]["publication_year"], 
            response.data[1]["publication_year"]
        )
