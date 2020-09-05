from django.urls import path
from meetings.views import details, room_list, create

urlpatterns = [
    path('create', create, name="create"),
    path('rooms', room_list, name="rooms"),
    path('<int:id>', details, name="meeting"),
]