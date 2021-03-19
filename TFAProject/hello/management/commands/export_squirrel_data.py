from django.core.management.base import BaseCommand
import csv
from hello.models import squirrel_data
import datetime
import pandas as pd



class Command(BaseCommand):
    def add_arguments(self,parser):
        parser.add_argument('file_location', type= str, help="Enter a valid file location")

    
    def handle(self, *args, **options):
        print("export_squirrel_data : is running", options["file_location"])
        df = pd.DataFrame(list(squirrel_data.objects.all().values()))
        del df['id']
        df.Date = df.Date.apply(lambda x: x.strftime('%m%d%Y')).astype(int)
        print(df.head())
        df.to_csv(options["file_location"], index = False)