from django.shortcuts import render, get_object_or_404

# Create your views here.
from meetings.models import Meeting


def details(request, id):
    contexts = {'meeting': get_object_or_404(Meeting, pk=id)}
    return render(request, 'meetings/details.html', contexts)