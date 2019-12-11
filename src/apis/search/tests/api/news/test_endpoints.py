from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

class NewsEndpointTest(APITestCase):

    @classmethod
    def setUp(self):
        super().setUpClass()

        self.url =reverse(
            'api_news:retrieve_news_by_keywords'
        )

    def test_get_news(self):
        data = {
            "keywords": ["one", "two", "three"]
        }

        response = self.client.get(self.url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
