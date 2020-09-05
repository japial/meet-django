from django.shortcuts import render, get_object_or_404, redirect
from meetings.models import Meeting, Room
from .forms import MeetingForm


def create(request):
    if request.method == "POST":
        form = MeetingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('welcome')
    else:
        form = MeetingForm
    return render(request, 'meetings/create.html', {'form': form})


def details(request, id):
    contexts = {'meeting': get_object_or_404(Meeting, pk=id)}
    return render(request, 'meetings/details.html', contexts)


def room_list(request):
    contexts = {'rooms': Room.objects.all()}
    return render(request, 'meetings/rooms.html', contexts)