from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from rooms.models import Room
from . models import Post
from .forms import PostForm


# Create your views here.



@login_required(login_url='login')
def createPost(request, pk):
    form = PostForm()
    post_room = Room.objects.get(id=pk)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.room = post_room               
            instance.room.participants.add(request.user)
            try:
                form.save()
                messages.success(request, 'Post published')
                return redirect('room_id', post_room.id)
            except:
                messages.error(request, 'Whoops something went wrong')
                return redirect('room_id', post_room.id)
        
    context = {'form':form}
    return render(request, 'posts/post_form.html', context)

@login_required(login_url='login')
def editPost(request, pk):
    post = Post.objects.get(id=pk)
    room_id = post.room.id
    form = PostForm(instance=post)

    if request.user != post.author:
        messages.error(request, 'User access denied')

    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.edited = True
            form.save()
            messages.success(request, 'Post Edited')
            return redirect('room_id', room_id)
    
    context = {'form':form}
    return render(request, 'posts/post_form.html', context)

@login_required(login_url='login')
def deletePost(request, pk):
    post = Post.objects.get(id=pk)
    room = post.room.id

    if request.user != post.author:
        return HttpResponse('User access denied')

    if request.method == "POST":
        post.delete()
        return redirect('home')

    return render(request, 'delete.html', {'obj':post})

@login_required(login_url='login')
def likePost(request, pk):
    post = Post.objects.get(id=pk)
    room = post.room.id
    user = request.user
    if user in post.likes.all():
        post.likes.remove(user)
    else:
        post.likes.add(user)
    return redirect('room_id',room)

@login_required(login_url='login')
def dislikePost(request, pk):
    post = Post.objects.get(id=pk)
    room = post.room.id
    user = request.user
    if user in post.dislikes.all():
        post.dislikes.remove(user)
    else:
        post.dislikes.add(user)
    return redirect('room_id',room)