from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
from meetings.models import Meeting


def welcome(request):
    contexts = {
        'message': 'Your Another Meeting Platform!',
        'total_meetings': Meeting.objects.count(),
        'meetings': Meeting.objects.all(),
    }
    return render(request, 'website/welcome.html', contexts)


def about(request):
    return HttpResponse(f"We are the developers of meeting planner app {datetime.now()}")