"""Patterns for room crud urls"""
from django.urls import path, include
from . import views

urlpatterns = [
    path('edit/<str:pk>', views.edit_room, name="edit_room"),
    path('create', views.create_room, name="create_room"),
    path('delete/<str:pk>', views.delete_room, name="delete_room"),
    path('<int:pk>', views.room, name="room_id"),
    path('post/', include('posts.urls'), name="post"),
]
