from django.shortcuts import render
from .models import FlickrAlbums

# Create your views here.

def index(request):
    links = FlickrAlbums.objects.all()
    context = {
        'links' : links,
    }
    return render(request, 'pictures/index.html', context)
