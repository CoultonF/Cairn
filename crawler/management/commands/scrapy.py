from django.core.management.base import BaseCommand

class Command(BaseCommand):    
    help = 'Scrapy commands. Accessible from: "Django manage.py". '

    def __init__(self, stdout=None, stderr=None, no_color=False):
        super().__init__(stdout=None, stderr=None, no_color=False)

        # Optional attribute declaration.
        self.no_color = no_color
        self.stderr = stderr
        self.stdout = stdout

        # Actual declaration of CLI command
        self._argv = None

    def run_from_argv(self, argv):
        self._argv = argv
        self.execute(stdout=None, stderr=None, no_color=False)

    def handle(self, *args, **options):
        from scrapy.cmdline import execute
        execute(self._argv[1:])