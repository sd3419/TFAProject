from django.shortcuts import render
from hello.models import squirrel_data

# Create your views here.
def index(request):
    return render(request, 'hello/index.html')

def map_(request):
    sightings = list(squirrel_data.objects.all().values())[:100]
    return render(request,'hello/map.html', {'sightings':sightings})

