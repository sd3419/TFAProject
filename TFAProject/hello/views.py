from django.shortcuts import render, redirect
from hello.models import squirrel_data
from .forms import SquirreldataForm
import pandas as pd
from django.views.decorators.csrf import ensure_csrf_cookie
from django.contrib import messages


# Create your views here.
def map(request):
    '''
    Returns the sighting details to be displayed in the map
    '''
    sightings = list(squirrel_data.objects.all().values())[:100]
    return render(request,'hello/map.html', {'sightings':sightings})

def sightings(request):
    '''
    Returns the sighting details to be displayed in the /sightings route
    '''
    sightings = list(squirrel_data.objects.all().values())
    return render(request, 'hello/sighting.html', {'sightings':sightings})

def update_sighting(request, unique_squirrel_id):
    '''
    Handles POST request and returns the 6 fields to be displayed in the Update Sightings page
    '''
    sightings = list(
        squirrel_data.objects.filter(unique_squirrel_id=unique_squirrel_id).values('x', 'y', 'unique_squirrel_id','shift', 'date', 'age'))

    if(request.method == "POST"):
        t = squirrel_data.objects.get(unique_squirrel_id= unique_squirrel_id)
        t.x = request.POST.get("x","")  # change field
        t.y = request.POST.get("y","")
        t.date = request.POST.get("date","")
        t.age = request.POST.get("age","")
        t.shift = request.POST.get("shift", "")
        t.unique_squirrel_id = request.POST.get("unique_squirrel_id", "")
        t.save()  # this will update only
        response = redirect('/sightings/'+t.unique_squirrel_id)
        messages.success(request, 'Form submission successful!')
        return response

    return render(request, 'hello/update_sighting.html', {'sightings': sightings})

@ensure_csrf_cookie
def squirrel_data_create(request):
    '''
    Handles POST request in the add sighting page
    '''
    form = SquirreldataForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Form submission successful')
    return render(request,"hello/index.html", {'form': form})

def display_r(request):
    '''
    Returns the values to be displayed on the Statistics page
    '''
    st = squirrel_data.objects.all()  # Collect all records from table

    df = pd.DataFrame(list(squirrel_data.objects.all().values()))
    percentage_running = df['running'].value_counts(normalize=True) * 100
    percentage_chasing = df['chasing'].value_counts(normalize=True) * 100
    percentage_climbing = df['climbing'].value_counts(normalize=True) * 100
    var1 = percentage_running[1].round()
    var2 = df.primary_fur_color.mode()[0]
    var3 = df['location'].value_counts()[1]
    var4 = percentage_chasing[1].round()
    var5 = percentage_climbing[1].round()

    return render(request, "hello/display.html", {'var1':var1,'var2':var2,'var3':var3,'var4':var4,'var5':var5})

def home(request):
    '''
    Function linked to the home page HTML
    '''
    return render(request, "hello/home_page.html")