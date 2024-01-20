"""Rooms Views"""
from django.shortcuts import render, redirect, get_object_or_404
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from posts.models import Post
from comments.forms import CommentForm
from . forms import RoomForm
from . models import Room


@login_required(login_url='login')
def create_room(request):
    """Creates Room"""
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

    context = {'form': form}
    return render(request, 'rooms/room_form.html', context)


@login_required(login_url='login')
def room(request, pk):
    """Renders room.html"""
    room_id = get_object_or_404(Room, id=pk)
    rooms = Room.objects.all()
    posts = room_id.post_room.all()
    comment_form = CommentForm
    participants = room_id.participants.all()
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.status = 1
            post_pk = request.POST.get('post')
            instance.post = Post.objects.get(id=post_pk)
            form.save()
    context = {'room': room_id,
               'posts': posts,
               'rooms': rooms,
               'comment_form': comment_form,
               'participants': participants,
               }
    return render(request, 'rooms/room.html', context)


@login_required(login_url='login')
def edit_room(request, pk):
    """Handles Editting of Room"""
    room_id = get_object_or_404(Room, id=pk)
    form = RoomForm(instance=room_id)

    if request.user != room_id.host:
        raise PermissionDenied

    if request.method == "POST":
        form = RoomForm(request.POST, instance=room_id)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(request, 'rooms/room_form.html', context)


@login_required(login_url='login')
def delete_room(request, pk):
    """Handles request to delete room"""
    room_id = get_object_or_404(Room, id=pk)
    if request.user != room.host:
        raise PermissionDenied
    if request.method == "POST":
        room.delete()
        return redirect('home')

    return render(request, 'delete.html', {'obj': room_id})
