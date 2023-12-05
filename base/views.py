from django.shortcuts import render
from django.db.models import Q
from django.views import View
from posts.models import Post
from comments.models import Comment
from rooms.models import Room, Topic
from friends.models import FriendRequest


def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    rooms = Room.objects.filter(
        Q(topic__name__icontains=q) |
        Q(name__icontains=q) |
        Q(description__icontains=q) |
        Q(host__username__icontains=q)
                                )
    
    room_count = rooms.count()
    topics = Topic.objects.all()
    posts = Post.objects.all()
    comments = Comment.objects.all()
    friend_data = FriendRequest.objects.all()
    context = {'posts':posts, 'comments':comments, 'topics':topics, 'rooms':rooms, 'room_count':room_count, 'friend_data': friend_data,}
    return render(request, 'base/home.html', context)

    
