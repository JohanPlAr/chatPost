from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('room/', include('rooms.urls'), name="room"),
    path('post/', include('posts.urls'), name="post"),
    
    ]

