from django.core.management.base import BaseCommand

from programs.services import sync_program_catalog


class Command(BaseCommand):
    help = "Synchronize program records from the code-managed program catalog."

    def add_arguments(self, parser):
        parser.add_argument(
            "--prune",
            action="store_true",
            help="Delete program records that are not present in the catalog.",
        )

    def handle(self, *args, **options):
        stats = sync_program_catalog(prune=options["prune"])
        summary = (
            f"Programs synchronized: {stats['created']} created, "
            f"{stats['updated']} updated, {stats['deleted']} deleted."
        )
        self.stdout.write(self.style.SUCCESS(summary))

