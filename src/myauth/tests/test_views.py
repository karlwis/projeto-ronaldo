from django.test import TestCase
from django.urls import reverse


class HomeViewTest(TestCase):
    def test_home_returns_200_and_expected_content(self):
        response = self.client.get(reverse('home'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Projeto Ronaldo')

    def test_home_rejects_post(self):
        response = self.client.post(reverse('home'))

        self.assertEqual(response.status_code, 405)

    def test_home_returns_html_content_type(self):
        response = self.client.get(reverse('home'))

        self.assertEqual(response['Content-Type'], 'text/html; charset=utf-8')
