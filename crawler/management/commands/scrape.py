from django.core.management.base import BaseCommand, CommandError
from bs4 import BeautifulSoup

class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def add_arguments(self, parser):
        parser.add_argument('url', nargs='?', type=str)

    def handle(self, *args, **options):
        print(options['url'])