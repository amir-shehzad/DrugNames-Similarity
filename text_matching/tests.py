from django.test import TestCase
from django.urls import reverse  # new
from rest_framework import status  # new
from .views import SearchView


class TextMatchingTest(TestCase):
    def test_api_listview(self):  # new
        response = self.client.get(reverse("index"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_similar(self):
        obj = SearchView()
        self.assertEqual(obj.similar("I love my coding", "i do love coding"), 0.75)

    def test_api_searchview(self):  # new
        response = self.client.get(reverse("search_values"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
