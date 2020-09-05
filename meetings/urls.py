from django.urls import path
from meetings.views import details, room_list

urlpatterns = [
    path('rooms', room_list, name="rooms"),
    path('<int:id>', details, name="meeting"),
]