from django.core.management.base import BaseCommand
import csv
from hello.models import squirrel_data
import datetime



class Command(BaseCommand):
    def add_arguments(self,parser):
        parser.add_argument('file_location', type= str, help="Enter a valid file location")
    
    
    def handle(self, *args, **options):
        print("import_squirrel_data : is running", options["file_location"])
        with open(options["file_location"]) as file_:
            reader = csv.reader(file_)
            next(reader)
            for row in reader:
                try:

                    a = squirrel_data(row[0],row[1],row[2],row[3],row[4],datetime.datetime.strptime(row[5], '%m%d%Y').date(),row[6],row[7],row[8],
                                      row[9],row[10],row[11],row[12],row[13],row[14],
                                      row[15].capitalize(),row[16].capitalize(),row[17].capitalize(),row[18].capitalize(),row[19].capitalize(),
                                      row[20],
                                      row[21].capitalize(),row[22].capitalize(),row[23].capitalize(),row[24].capitalize(),row[25].capitalize(),row[26].capitalize(),
                                      row[27].capitalize(),row[28].capitalize(),row[29])
                    a.save()
                except Exception as e:
                    print("Exception:", e)


