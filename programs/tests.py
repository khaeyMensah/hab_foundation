from unittest.mock import patch

from django.db import OperationalError
from django.test import TestCase
from django.urls import reverse

from .models import Program
from .services import get_programs


class ProgramPageTests(TestCase):
    def test_programs_page_loads(self):
        response = self.client.get(reverse("programs:list"))
        self.assertEqual(response.status_code, 200)

    def test_programs_page_displays_program_content(self):
        Program.objects.create(
            title="Education Support",
            slug="education-support",
            description="Helping students with learning materials.",
            category="Education",
        )

        response = self.client.get(reverse("programs:list"))

        self.assertContains(response, "Education Support")
        self.assertContains(response, "Helping students with learning materials.")

    @patch("programs.services.Program.objects.order_by", side_effect=OperationalError)
    def test_get_programs_returns_empty_list_when_table_is_unavailable(self, mocked_order_by):
        programs = get_programs()

        self.assertEqual(programs, [])
        mocked_order_by.assert_called_once_with("title")

# Create your tests here.
