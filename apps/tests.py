from django.test import TestCase
from django.urls import reverse

from .models import ContactMessage


class PublicPagesTests(TestCase):
    def test_public_pages_are_available(self):
        for name in ('home', 'about', 'services', 'portfolio', 'certificates', 'contact'):
            with self.subTest(page=name):
                response = self.client.get(reverse(name))
                self.assertEqual(response.status_code, 200)

    def test_navigation_keeps_selected_language(self):
        response = self.client.get('/ru/')

        self.assertContains(response, 'href="/ru/about/"')
        self.assertContains(response, 'href="/ru/services/"')

    def test_contact_message_is_saved(self):
        response = self.client.post(
            reverse('contact'),
            {
                'name': 'Test User',
                'phone': '+998 90 000 00 00',
                'email': 'test@example.com',
                'message': 'Test message',
            },
        )

        self.assertRedirects(response, reverse('contact'))
        self.assertEqual(ContactMessage.objects.count(), 1)

    def test_incomplete_contact_message_is_not_saved(self):
        response = self.client.post(reverse('contact'), {'name': 'Test User'})

        self.assertEqual(response.status_code, 200)
        self.assertFalse(ContactMessage.objects.exists())

    def test_contact_phone_rejects_letters(self):
        response = self.client.post(
            reverse('contact'),
            {
                'name': 'Test User',
                'phone': 'ASDF123',
                'email': 'test@example.com',
                'message': 'Test message',
            },
        )

        self.assertEqual(response.status_code, 200)
        self.assertFalse(ContactMessage.objects.exists())
