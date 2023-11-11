from django.shortcuts import render
from django.views import View
from posts.models import Post, Comment
from rooms.models import Room,


def home(request):
    rooms= Room.objects.all()
    posts= Post.objects.all()
    comments = Comment.objects.all()
    context = {'posts':posts, 'comments':comments, 'rooms':rooms}
    return render(request, 'base/home.html', context)

    
