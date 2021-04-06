from django.shortcuts import render
from hello.models import squirrel_data
from .forms import SquirreldataForm
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

def squirrel_data_create(request):
    form = SquirreldataForm(request.POST or None)
    if form.is_valid():
        form.save()
    return render(request,"hello/index.html", {'form': form})

def display_r(request):
    st = squirrel_data.objects.all()  # Collect all records from table
    return render(request, "hello/display.html", {'st': st})