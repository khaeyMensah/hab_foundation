from django.db import OperationalError, ProgrammingError

from .catalog import PROGRAM_CATALOG
from .models import Program


def get_programs(ordering="title", limit=None):
    """
    Return program records safely.

    During first-time setup or before migrations are applied, the Program table
    may not exist yet. In that case we return an empty list so public pages
    still render instead of failing with a 500 error.
    """
    try:
        queryset = Program.objects.order_by(ordering)
        if limit is not None:
            queryset = queryset[:limit]
        return list(queryset)
    except (OperationalError, ProgrammingError):
        return []


def sync_program_catalog(program_data=None, prune=False):
    """
    Sync program records from a code-managed catalog into the database.

    The slug is treated as the stable identifier, so editing the title,
    description, or category in development will update the matching record
    in production the next time this sync runs.
    """
    catalog = list(program_data or PROGRAM_CATALOG)
    _validate_program_catalog(catalog)

    created = 0
    updated = 0
    catalog_slugs = []

    for item in catalog:
        catalog_slugs.append(item["slug"])
        _, was_created = Program.objects.update_or_create(
            slug=item["slug"],
            defaults={
                "title": item["title"],
                "description": item["description"],
                "category": item["category"],
            },
        )

        if was_created:
            created += 1
        else:
            updated += 1

    deleted = 0
    if prune:
        deleted, _ = Program.objects.exclude(slug__in=catalog_slugs).delete()

    return {
        "created": created,
        "updated": updated,
        "deleted": deleted,
        "catalog_size": len(catalog),
    }


def _validate_program_catalog(catalog):
    seen_slugs = set()
    required_keys = {"title", "slug", "description", "category"}

    for index, item in enumerate(catalog, start=1):
        missing_keys = required_keys.difference(item)
        if missing_keys:
            missing_fields = ", ".join(sorted(missing_keys))
            raise ValueError(f"Program catalog item {index} is missing: {missing_fields}")

        slug = item["slug"]
        if slug in seen_slugs:
            raise ValueError(f"Duplicate program slug found in catalog: {slug}")
        seen_slugs.add(slug)
