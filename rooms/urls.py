from django.urls import path, include
from . import views

urlpatterns = [
    path('edit/<str:pk>', views.editRoom, name="edit_room"),
    path('create', views.createRoom, name="create_room"),
    path('delete/<str:pk>', views.deleteRoom, name="delete_room"),
    path('<int:pk>', views.room, name="room_id"),
    path('post/', include('posts.urls'), name="post"),
    ]