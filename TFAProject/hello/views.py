from django.shortcuts import render
from hello.models import squirrel_data
from .forms import SquirreldataForm
import pandas as pd
from django.views.decorators.csrf import ensure_csrf_cookie

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
   

@ensure_csrf_cookie
def squirrel_data_create(request):
    form = SquirreldataForm(request.POST or None)
    if form.is_valid():
        form.save()
    return render(request,"hello/index.html", {'form': form})

def display_r(request):
    st = squirrel_data.objects.all()  # Collect all records from table

    df = pd.DataFrame(list(squirrel_data.objects.all().values()))
    percentage_running = df['Running'].value_counts(normalize=True) * 100
    var1 = percentage_running[0].round()

    var2 = df.Primary_Fur_Color.mode()[0]

    var3 = df['Location'].value_counts()[1]

    return render(request, "hello/display.html", {'var1':var1,'var2':var2,'var3':var3})