from django.core.management.base import BaseCommand

class Command(BaseCommand):
    def add_arguments(self,parser):
        parser.add_argument('file_location', type= str, help="Enter a valid file location")
    
    
    def handle(self, *args, **options):
        print("import_squirrel_data : is running", options["file_location"])
        with open(options["file_location"]) as file_:
            reader = csv.reader(file_):
            
        