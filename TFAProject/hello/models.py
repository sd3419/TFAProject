from django.db import models

# Create your models here.
class squirrel_data(models.Model):
    X = models.FloatField()
    Y = models.FloatField()
    Unique_Squirrel_ID = models.CharField(max_length=256)
    Hectare = models.CharField(max_length=256)
    Shift = models.CharField(max_length=2)
    Date = models.DateField(max_length=256)
    Hectare_Squirrel_Number = models.IntegerField()
    Age = models.CharField(max_length=256)
    Primary_Fur_Color = models.CharField(max_length=256)
    Highlight_Fur_Color = models.CharField(max_length=256)
    Combination_of_Primary_and_Highlight_Color = models.CharField(max_length=256)
    Color_notes = models.CharField(max_length=256)
    Location = models.CharField(max_length=256)
    Above_Ground_Sighter_Measurement = models.CharField(max_length=256)
    Specific_Location = models.CharField(max_length=256)
    Running= models.BooleanField()
    Chasing = models.BooleanField()
    Climbing = models.BooleanField()
    Eating = models.BooleanField()
    Foraging = models.BooleanField()
    Other_Activities = models.CharField(max_length=256)
    Kuks = models.BooleanField()
    Quaas = models.BooleanField()
    Moans = models.BooleanField()
    Tail_flags = models.BooleanField()
    Tail_twitches = models.BooleanField()
    Approaches = models.BooleanField()
    Indifferent = models.BooleanField()
    Runs_from = models.BooleanField()
    Other_Interactions = models.CharField(max_length=256)
    Lat_Long = models.CharField(max_length=256)

    def __str__(self):
        return self.Unique_Squirrel_ID

    def add_data_row(self, row_json):#row is a json
        pass








