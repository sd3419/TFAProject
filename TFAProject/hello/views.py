from django.shortcuts import render
from hello.models import squirrel_data

# Create your views here.
def index(request):
    return render(request, 'hello/index.html')

def map_(request):
    sightings = list(squirrel_data.objects.all().values())[:100]
    return render(request,'hello/map.html', {'sightings':sightings})

def sightings(request):
    sightings = list(squirrel_data.objects.all().values('Unique_Squirrel_ID', 'Date'))
    return render(request, 'hello/sighting.html', {'sightings':sightings})

def update_sighting(request, unique_squirrel_id):
    sightings = list(squirrel_data.objects.filter(Unique_Squirrel_ID = unique_squirrel_id).values('X', 'Y','Unique_Squirrel_ID', 'Shift', 'Date', 'Age'))
    return render(request, 'hello/update_sighting.html', {'sightings': sightings})