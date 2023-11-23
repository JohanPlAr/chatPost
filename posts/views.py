from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from . models import Post
from comments.models import Comment
from .forms import PostForm


# Create your views here.



@login_required(login_url='login')
def createPost(request):
    form = PostForm()
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        
    context = {'form':form}
    return render(request, 'posts/post_form.html', context)


@login_required(login_url='login')
def editPost(request, pk):
    post = Post.objects.get(id=pk)
    form = PostForm(instance=post)

    if request.user != post.author:
        return HttpResponse('User access denied')

    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('home')
    
    context = {'form':form}
    return render(request, 'posts/post_form.html', context)

@login_required(login_url='login')
def deletePost(request, pk):
    post = Post.objects.get(id=pk)

    if request.user != post.author:
        return HttpResponse('User access denied')

    if request.method == "POST":
        post.delete()
        return redirect('home')

    return render(request, 'rooms/delete.html', {'obj':post})

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