"""
Django command to wait for the database to be available.
"""


import time

from psycopg2 import OperationalError as Psycopg2opError

from django.db.utils import OperationalError
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """Django command to wait for database."""

    def handle(self, *args, **options):
        """Entrycomand for command."""
        self.stdout.write('Waiting for database...')
        db_up = False
        while db_up is False:
            try:
                self.check(databases=['default'])
                db_up = True
            except (OperationalError, Psycopg2opError) as error:
                self.stdout.write(f'Database is anavailable - {error} \n waiting for 1 second...')
            time.sleep(1)
        self.stdout.write(self.style.SUCCESS('Connected successfully to databese!'))
