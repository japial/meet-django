from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def welcome(request):
    return HttpResponse('Welcome to meeting Planner')


def about(request):
    return HttpResponse(f"We are the developers of meeting planner app {datetime.now()}")