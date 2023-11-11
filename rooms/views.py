from django.shortcuts import render, redirect, HttpResponse
from . forms import RoomForm
from . models import Room
from posts.models import Post 

# Create your views here.
def createRoom(request):
    form = RoomForm()
    if request.method == "POST":
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        
    context = {'form':form}
    return render(request, 'rooms/room_form.html', context)

def room(request, pk):
    posts = Post.objects.all()
    room = Room.objects.get(id=pk)
    context = {'room': room, 'posts':posts,}
    return render(request, 'rooms/room.html', context)

def editRoom(request, pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)
    if request.method == "POST":
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')
    
    context = {'form':form}
    return render(request, 'rooms/room_form.html', context)

def deleteRoom(request, pk):
    room = Room.objects.get(id=pk)
    if request.method == "POST":
        room.delete()
        return redirect('home')

    return render(request, 'rooms/delete.html', {'obj':room})