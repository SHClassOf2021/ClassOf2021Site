from django.shortcuts import render
from .models import Officer

# Create your views here.

def index(request):
    list_of_officers = Officer.objects.all()
    context = {
        "list_of_officers" : list_of_officers,
    }
    return render(request, 'contact/index.html', context)
