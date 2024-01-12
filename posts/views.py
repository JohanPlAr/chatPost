from django.shortcuts import render, redirect, get_object_or_404
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from rooms.models import Room
from . models import Post
from .forms import PostForm
from chatPost.context_processors import globalContext


@login_required(login_url = 'login') 
def createPost(request, pk):
    friends_list = globalContext(request)["friends_list"]
    form = PostForm()
    post_room = get_object_or_404(Room, id = pk)
    friends_list = globalContext(request)["friends_list"]
    if request.user != post_room.host:
        if post_room.status == 1 and post_room.host not in friends_list:
            raise PermissionDenied
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit = False)
            instance.author = request.user
            instance.room = post_room              
            instance.room.participants.add(request.user)
            try:
                form.save()
                messages.success(request, 'Post published')
                return redirect('room_id', post_room.id)
            except:
                messages.error(request, 'Oops something went wrong')
                return redirect('room_id', post_room.id)
        
    context = {'form':form, 'post_room':post_room}
    return render(request, 'posts/post_form.html', context)


@login_required(login_url = 'login')
def editPost(request, pk):
    post = get_object_or_404(Post, id = pk)
    room_id = post.room.id
    form = PostForm(instance = post)
    if request.user != post.author:
        raise PermissionDenied
    else:
        if request.method == "POST":
            form = PostForm(request.POST, request.FILES, instance = post)
            if form.is_valid():
                instance = form.save(commit = False)
                instance.edited = True
                instance.save()
                messages.success(request, 'Post Edited')
            else:
                messages.error(request, form.errors)
            return redirect('room_id', room_id)
    context = {'form':form}
    return render(request, 'posts/post_form.html', context)


@login_required(login_url = 'login')
def deletePost(request, pk):
    post = Post.objects.get(id = pk)
    room_id = post.room.id
    if request.user != post.author:
        raise PermissionDenied
    else:
        if request.method == "POST":
            post.delete()
            return redirect('room_id', room_id)

    return render(request, 'delete.html', {'obj':post})


@login_required(login_url = 'login')
def likePost(request, pk):
    post = get_object_or_404(Post, id = pk)
    room = post.room.id
    user = request.user
    if user in post.likes.all():
        post.likes.remove(user)
    else:
        post.likes.add(user)
    return redirect('room_id',room)


@login_required(login_url = 'login')
def dislikePost(request, pk):
    post = get_object_or_404(Post, id = pk)
    room = post.room.id
    user = request.user
    if user in post.dislikes.all():
        post.dislikes.remove(user)
    else:
        post.dislikes.add(user)
    return redirect('room_id',room)