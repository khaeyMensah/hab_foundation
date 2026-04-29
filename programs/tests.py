from io import StringIO
from unittest.mock import patch

from django.core.management import call_command
from django.db import OperationalError
from django.test import TestCase
from django.urls import reverse

from .catalog import PROGRAM_CATALOG
from .models import Program
from .services import get_programs, sync_program_catalog


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


class ProgramSyncTests(TestCase):
    def test_sync_program_catalog_creates_records_from_custom_catalog(self):
        Program.objects.all().delete()

        stats = sync_program_catalog(
            program_data=[
                {
                    "title": "Health Outreach",
                    "slug": "health-outreach",
                    "description": "Community care and screening.",
                    "category": "Health",
                },
                {
                    "title": "Youth Skills",
                    "slug": "youth-skills",
                    "description": "Skills support for youth.",
                    "category": "Empowerment",
                },
            ]
        )

        self.assertEqual(stats["created"], 2)
        self.assertEqual(stats["updated"], 0)
        self.assertEqual(stats["deleted"], 0)
        self.assertEqual(Program.objects.count(), 2)

    def test_sync_program_catalog_updates_existing_records_and_can_prune(self):
        Program.objects.all().delete()

        Program.objects.create(
            title="Old Title",
            slug="health-outreach",
            description="Old description",
            category="Old category",
        )
        Program.objects.create(
            title="Remove Me",
            slug="remove-me",
            description="This record should be pruned.",
            category="Other",
        )

        stats = sync_program_catalog(
            program_data=[
                {
                    "title": "Health Outreach Updated",
                    "slug": "health-outreach",
                    "description": "Updated community care and screening.",
                    "category": "Health",
                }
            ],
            prune=True,
        )

        program = Program.objects.get(slug="health-outreach")

        self.assertEqual(stats["created"], 0)
        self.assertEqual(stats["updated"], 1)
        self.assertEqual(stats["deleted"], 1)
        self.assertEqual(program.title, "Health Outreach Updated")
        self.assertEqual(program.description, "Updated community care and screening.")
        self.assertFalse(Program.objects.filter(slug="remove-me").exists())

    def test_sync_programs_command_loads_default_catalog(self):
        Program.objects.all().delete()
        stdout = StringIO()

        call_command("sync_programs", stdout=stdout)

        self.assertEqual(Program.objects.count(), len(PROGRAM_CATALOG))
        self.assertIn("Programs synchronized", stdout.getvalue())
