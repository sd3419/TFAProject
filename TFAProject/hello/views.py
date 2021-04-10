from django.shortcuts import render, redirect
from hello.models import squirrel_data
from .forms import SquirreldataForm
import pandas as pd
from django.views.decorators.csrf import ensure_csrf_cookie
from django.contrib import messages


# Create your views here.
def index(request):
    return render(request, 'hello/index.html')

def map_(request):
    sightings = list(squirrel_data.objects.all().values())[:100]
    return render(request,'hello/map.html', {'sightings':sightings})

def sightings(request):
    sightings = list(squirrel_data.objects.all().values())
    return render(request, 'hello/sighting.html', {'sightings':sightings})
    if(reqest.method == "POST"):
        t = squirrel_data.objects.all()
        return render(request, "hello/display.html",{'t':t})


def update_sighting(request, unique_squirrel_id):
    sightings = list(
        squirrel_data.objects.filter(unique_squirrel_id=unique_squirrel_id).values('x', 'y', 'unique_squirrel_id',
                                                                                   'shift', 'date', 'age'))

    if(request.method == "POST"):
        t = squirrel_data.objects.get(unique_squirrel_id= unique_squirrel_id)
        t.X = request.POST.get("x","")  # change field
        t.Y = request.POST.get("y","")
        t.Date = request.POST.get("date","")
        t.Age = request.POST.get("age","")
        t.Unique_Squirrel_ID = request.POST.get("unique_squirrel_id", "")
        t.save()  # this will update only
        messages.success(request, 'Form submission successful')
        response = redirect('/sightings/'+t.Unique_Squirrel_ID)
        return response

    return render(request, 'hello/update_sighting.html', {'sightings': sightings})

@ensure_csrf_cookie
def squirrel_data_create(request):
    form = SquirreldataForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Form submission successful')
    return render(request,"hello/index.html", {'form': form})

def display_r(request):
    st = squirrel_data.objects.all()  # Collect all records from table

    df = pd.DataFrame(list(squirrel_data.objects.all().values()))
    percentage_running = df['Running'].value_counts(normalize=True) * 100
    percentage_chasing = df['Chasing'].value_counts(normalize=True) * 100
    percentage_climbing = df['Climbing'].value_counts(normalize=True) * 100
    var1 = percentage_running[1].round()
    var2 = df.Primary_Fur_Color.mode()[0]
    var3 = df['Location'].value_counts()[1]
    var4 = percentage_chasing[1].round()
    var5 = percentage_climbing[1].round()

    return render(request, "hello/display.html", {'var1':var1,'var2':var2,'var3':var3,'var4':var4,'var5':var5})

def view_data(request, unique_squirrel_id):
    st = list(squirrel_data.objects.filter(Unique_Squirrel_ID = unique_squirrel_id).values())
    return render(request, "hello/view.html", {'st': st})