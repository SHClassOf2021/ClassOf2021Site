from django.shortcuts import render
from django.http import HttpResponse
from .models import Announcement

# Create your views here.

def index(request):
    latest_announcements = Announcement.objects.order_by('-pub_date')[:4]
    context = {
        'latest_announcements' : latest_announcements,
    }
    return render(request, 'home/index.html', context)

def announcements(request):
    latest_announcements_all = Announcement.objects.order_by('-pub_date')[:]
    context = {
        'latest_announcements_all' : latest_announcements_all,
    }
    return render(request, 'home/announcements.html', context)
