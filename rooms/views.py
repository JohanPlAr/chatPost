from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . forms import RoomForm
from . models import Room, Topic
from comments.models import Comment
from comments.forms import CommentForm

# Create your views here.

@login_required(login_url='login')
def createRoom(request):
    form = RoomForm()
    if request.method == "POST":
        form = RoomForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.host = request.user
            instance.save()
            instance.participants.add(request.user)
            return redirect('home')
        
    context = {'form':form}
    return render(request, 'rooms/room_form.html', context)

@login_required(login_url='login')
def room(request, pk):
    room = Room.objects.get(id=pk)
    rooms = Room.objects.all()
    posts = room.post_room.all()
    comment_form = CommentForm
    comments = Comment.objects.all()
    topics = Topic.objects.all()
    participants = room.participants.all()
    context = {'room': room, 
               'posts':posts, 
               'topics':topics, 
               'rooms':rooms, 
               'comments':comments,
               'comment_form': comment_form, 
               'participants':participants}
    return render(request, 'rooms/room.html', context)

@login_required(login_url='login')
def editRoom(request, pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)

    if request.user != room.host:
        return HttpResponse('User access denied')

    if request.method == "POST":
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')
    
    context = {'form':form}
    return render(request, 'rooms/room_form.html', context)

@login_required(login_url='login')
def deleteRoom(request, pk):
    room = Room.objects.get(id=pk)
    if request.user != room.host:
        return HttpResponse('User access denied')
    if request.method == "POST":
        room.delete()
        return redirect('home')

    return render(request, 'rooms/delete.html', {'obj':room})

