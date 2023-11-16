from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . forms import RoomForm
from . models import Room
from posts.models import Post 

# Create your views here.

@login_required(login_url='login')
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
    room = Room.objects.get(id=pk)
    posts = room.post_room.all()
    context = {'room': room, 'posts':posts,}
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