from django.urls import path, include
from . import views

urlpatterns = [
    path('/<str:pk>', views.room, name="room"),
    path('/edit/<str:pk>', views.editRoom, name="edit_room"),
    path('/create', views.createRoom, name="create_room"),
    path('/delete/<str:pk>', views.deleteRoom, name="delete_room"),     
    ]