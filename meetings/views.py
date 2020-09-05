from django.shortcuts import render, get_object_or_404

# Create your views here.
from meetings.models import Meeting, Room


def details(request, id):
    contexts = {'meeting': get_object_or_404(Meeting, pk=id)}
    return render(request, 'meetings/details.html', contexts)


def room_list(request):
    contexts = {'rooms': Room.objects.all()}
    return render(request, 'meetings/rooms.html', contexts)