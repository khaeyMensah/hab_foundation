from django.db import OperationalError, ProgrammingError

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

