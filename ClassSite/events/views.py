from django.shortcuts import render
from .models import Event

# Create your views here.

def index(request):
    events = Event.objects.order_by('pub_date')[:]
    context = {
        'events' : events,
    }
    return render(request, 'events/index.html', context)
