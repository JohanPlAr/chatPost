from django.shortcuts import render, redirect, get_object_or_404
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . forms import RoomForm
from . models import Room
from posts.models import Post
from comments.forms import CommentForm
from django.contrib import messages

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
            messages.success(request, f"{instance} was successfully created")
            return redirect('room_id', instance.id)
        
    context = {'form':form}
    return render(request, 'rooms/room_form.html', context)

@login_required(login_url='login')
def room(request, pk):
    room = get_object_or_404(Room, id = pk)
    rooms = Room.objects.all() 
    posts = room.post_room.all()
    comment_form = CommentForm
    participants = room.participants.all()
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.status = 1
            post_pk = request.POST.get('post')
            instance.post = Post.objects.get(id=post_pk)
            form.save()
    context = {'room': room,
               'posts':posts, 
               'rooms':rooms, 
               'comment_form': comment_form, 
               'participants':participants,
               }
    return render(request, 'rooms/room.html', context)

@login_required(login_url='login')
def editRoom(request, pk):
    room = get_object_or_404(Room, id = pk)
    form = RoomForm(instance=room)

    if request.user != room.host:
        raise PermissionDenied

    if request.method == "POST":
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')
    
    context = {'form':form}
    return render(request, 'rooms/room_form.html', context)

@login_required(login_url='login')
def deleteRoom(request, pk):
    room = get_object_or_404(Room, id = pk)
    if request.user != room.host:
        raise PermissionDenied
    if request.method == "POST":
        room.delete()
        return redirect('home')

    return render(request, 'delete.html', {'obj':room})

