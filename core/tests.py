from django.test import TestCase
from django.urls import reverse


class CorePageTests(TestCase):
    def test_homepage_loads(self):
        response = self.client.get(reverse("core:home"))
        self.assertEqual(response.status_code, 200)

    def test_about_page_loads(self):
        response = self.client.get(reverse("core:about"))
        self.assertEqual(response.status_code, 200)

    def test_impact_page_loads(self):
        response = self.client.get(reverse("core:impact"))
        self.assertEqual(response.status_code, 200)

    def test_contact_page_loads(self):
        response = self.client.get(reverse("core:contact"))
        self.assertEqual(response.status_code, 200)

