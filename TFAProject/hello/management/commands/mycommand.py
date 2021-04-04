from django.core.management.base import BaseCommand

class Command(BaseCommand):
    def add_arguments(self,parser):
        parser.add_argument('first')
    
    
    def handle(self, *args, **options):
        print("mycommand : isss running", options["first"])