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
                a = squirrel_data()
                a.X = row[0]
                a.Y = row[1]
                a.Unique_Squirrel_ID = row[2]
                a.Hectare = row[3]
                a.Shift = row[4]
                a.Date = datetime.datetime.strptime(row[5], '%m%d%Y').date()
                a.Hectare_Squirrel_Number = row[6]
                a.Age = row[7]
                a.Primary_Fur_Color = row[8]
                a.Highlight_Fur_Color = row[9]
                a.Combination_of_Primary_and_Highlight_Color = row[10]
                a.Color_notes = row[11]
                a.Location = row[12]
                a.Above_Ground_Sighter_Measurement = row[13]
                a.Specific_Location = row[14]
                a.Running = row[15].capitalize()
                a.Chasing = row[16].capitalize()
                a.Climbing = row[17].capitalize()
                a.Eating = row[18].capitalize()
                a.Foraging = row[19].capitalize()
                a.Other_Activities = row[20]
                a.Kuks = row[21].capitalize()
                a.Quaas = row[22].capitalize()
                a.Moans = row[23].capitalize()
                a.Tail_flags = row[24].capitalize()
                a.Tail_twitches = row[25].capitalize()
                a.Approaches = row[26].capitalize()
                a.Indifferent = row[27].capitalize()
                a.Runs_from = row[28].capitalize()
                a.Other_Interactions = row[29]
                a.Lat_Long = row[30]
                a.save()
