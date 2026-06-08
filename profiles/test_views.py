from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from profiles.models import GameEntry


class ProfileViewTests(TestCase):
    """Tests for the profile view."""

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        self.client.login(username='testuser', password='testpass123')

    def test_profile_page_loads(self):
        """Profile page renders for authenticated user."""
        response = self.client.get(reverse('profile'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/profile.html')

    def test_profile_redirects_if_not_logged_in(self):
        """Profile page redirects unauthenticated users to login."""
        self.client.logout()
        response = self.client.get(reverse('profile'))
        self.assertEqual(response.status_code, 302)

    def test_profile_shows_correct_counts(self):
        """Profile page context contains correct entry counts."""
        GameEntry.objects.create(
            user=self.user, title='Zelda', platform='130',
            status='playing'
        )
        GameEntry.objects.create(
            user=self.user, title='Mario', platform='130',
            status='completed'
        )
        response = self.client.get(reverse('profile'))
        self.assertEqual(response.context['playing_count'], 1)
        self.assertEqual(response.context['completed_count'], 1)


class AllEntriesViewTests(TestCase):
    """Tests for the all entries view."""

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        self.client.login(username='testuser', password='testpass123')
        self.entry = GameEntry.objects.create(
            user=self.user, title='Zelda', platform='130',
            status='playing'
        )

    def test_all_entries_page_loads(self):
        """All entries page renders for authenticated user."""
        response = self.client.get(reverse('all_entries'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/all_entries.html')

    def test_all_entries_redirects_if_not_logged_in(self):
        """All entries page redirects unauthenticated users to login."""
        self.client.logout()
        response = self.client.get(reverse('all_entries'))
        self.assertEqual(response.status_code, 302)

    def test_all_entries_filter_by_status(self):
        """Status filter returns only entries with matching status."""
        GameEntry.objects.create(
            user=self.user, title='Mario', platform='130',
            status='completed'
        )
        response = self.client.get(
            reverse('all_entries'), {'status': 'playing'}
        )
        entries = response.context['entries']
        for entry in entries:
            self.assertEqual(entry.status, 'playing')


class RemoveEntryTests(TestCase):
    """Tests for the remove entry view."""

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        self.client.login(username='testuser', password='testpass123')
        self.entry = GameEntry.objects.create(
            user=self.user, title='Zelda', platform='130',
            status='playing'
        )

    def test_remove_entry_deletes_entry(self):
        """POST to remove entry deletes the entry from the database."""
        response = self.client.post(
            reverse('remove_entry', args=[self.entry.id])
        )
        self.assertFalse(GameEntry.objects.filter(id=self.entry.id).exists())

    def test_remove_entry_redirects_after_delete(self):
        """Remove entry redirects to all entries page after deletion."""
        response = self.client.post(
            reverse('remove_entry', args=[self.entry.id])
        )
        self.assertRedirects(response, reverse('all_entries'))

    def test_remove_entry_requires_post(self):
        """Remove entry returns 405 for GET requests."""
        response = self.client.get(
            reverse('remove_entry', args=[self.entry.id])
        )
        self.assertEqual(response.status_code, 405)

    def test_cannot_remove_another_users_entry(self):
        """A user cannot delete another user's entry."""
        other_user = User.objects.create_user(
            username='otheruser',
            password='testpass123'
        )
        other_entry = GameEntry.objects.create(
            user=other_user, title='Mario', platform='130',
            status='playing'
        )
        response = self.client.post(
            reverse('remove_entry', args=[other_entry.id])
        )
        self.assertEqual(response.status_code, 404)


class EditEntryViewTests(TestCase):
    """Tests for the edit entry view."""

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        self.client.login(username='testuser', password='testpass123')
        self.entry = GameEntry.objects.create(
            user=self.user, title='Zelda', platform='130',
            status='playing'
        )

    def test_edit_entry_page_loads(self):
        """Edit entry page renders for authenticated user."""
        response = self.client.get(
            reverse('edit_entry', args=[self.entry.id])
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/edit_entry.html')

    def test_edit_entry_updates_status(self):
        """POST to edit entry updates the entry status."""
        response = self.client.post(
            reverse('edit_entry', args=[self.entry.id]),
            {
                'status': 'completed',
                'date_started': '2024-01-01',
                'date_completed': '2024-06-01',
            }
        )
        self.entry.refresh_from_db()
        self.assertEqual(self.entry.status, 'completed')

    def test_cannot_edit_another_users_entry(self):
        """A user cannot edit another user's entry."""
        other_user = User.objects.create_user(
            username='otheruser',
            password='testpass123'
        )
        other_entry = GameEntry.objects.create(
            user=other_user, title='Mario', platform='130',
            status='playing'
        )
        response = self.client.get(
            reverse('edit_entry', args=[other_entry.id])
        )
        self.assertEqual(response.status_code, 404)
