from django.db import models

# Create your models here.
class squirrel_data(models.Model):
    x = models.FloatField()
    y = models.FloatField()
    unique_squirrel_id = models.CharField(max_length=256, primary_key=True, unique=True)
    hectare = models.CharField(max_length=256)
    shift = models.CharField(max_length=2, choices=(
        ('AM', 'AM'),
        ('PM', 'PM'),))
    date = models.DateField(max_length=256)
    hectare_squirrel_number = models.IntegerField()
    age = models.CharField(max_length=256, blank=True, null=True, choices=(
        ('Adult', 'Adult'),
        ('Juvenile', 'Juvenile'),))
    primary_fur_color = models.CharField(max_length=256, null=True, blank=True)
    highlight_fur_color = models.CharField(max_length=256, null=True, blank=True)
    combination_of_primary_and_highlight_color = models.CharField(max_length=256)
    color_notes = models.CharField(max_length=256, blank=True, null=True)
    location = models.CharField(max_length=256, null=True, blank=True, choices=(
        ('Above Ground', 'Above Ground'),
        ('Ground Plane', 'Ground Plane'),
        ('', 'blank'),))
    above_ground_sighter_measurement = models.CharField(max_length=256, null=True, blank=True)
    specific_location = models.CharField(max_length=256, null=True, blank=True)
    running = models.BooleanField()
    chasing = models.BooleanField()
    climbing = models.BooleanField()
    eating = models.BooleanField()
    foraging = models.BooleanField()
    other_activities = models.CharField(max_length=256, null=True, blank=True)
    kuks = models.BooleanField()
    quaas = models.BooleanField()
    moans = models.BooleanField()
    tail_flags = models.BooleanField()
    tail_twitches = models.BooleanField()
    approaches = models.BooleanField()
    indifferent = models.BooleanField()
    runs_from = models.BooleanField()
    other_interactions = models.CharField(max_length=256, null=True, blank=True)

    def __str__(self):
        return self.Unique_Squirrel_ID

    def add_data_row(self, row_json):#row is a json
        pass








