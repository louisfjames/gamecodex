from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from unittest.mock import patch


class SearchViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        self.client.login(username='testuser', password='testpass123')

    def test_search_page_loads(self):
        """Search page renders with no query parameters."""
        response = self.client.get(reverse('search'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'games/search.html')

    def test_search_no_query_returns_empty_results(self):
        """No query parameter returns an empty results list."""
        response = self.client.get(reverse('search'))
        self.assertEqual(response.context['results'], [])

    @patch('games.views.search_games')
    def test_search_with_valid_query(self, mock_search):
        """A valid query calls search_games and returns results."""
        mock_search.return_value = {
            "error": None,
            "results": [
                {
                    "name": "Zelda",
                    "platforms": [],
                }
            ]
        }
        response = self.client.get(reverse('search'), {'q': 'zelda'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['results']), 1)
        self.assertEqual(response.context['query'], 'zelda')

    @patch('games.views.search_games')
    def test_search_api_error_returned_in_context(self, mock_search):
        """An API error is passed through to the template context."""
        mock_search.return_value = {
            "error": "IGDB credentials missing.",
            "results": []
        }
        response = self.client.get(reverse('search'), {'q': 'zelda'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.context['error'], "IGDB credentials missing."
        )

    @patch('games.views.search_games')
    def test_platform_filter_passed_to_search(self, mock_search):
        """Platform filter is passed to search_games and returned in context."""
        mock_search.return_value = {"error": None, "results": []}
        response = self.client.get(
            reverse('search'), {'q': 'zelda', 'platform': 'Nintendo'}
        )
        self.assertEqual(response.context['platform'], 'Nintendo')
        mock_search.assert_called_once()