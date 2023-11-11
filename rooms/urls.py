from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.createRoom, name="create_room")
         ]