"""Comment Crud, Like and Dislike functions"""

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from posts.models import Post
from rooms.models import Room
from . models import Comment
from .forms import CommentForm
from chatPost.context_processors import globalContext


@login_required(login_url='login')
def createComment(request, pk):
    """Create Comment function"""
    form = CommentForm()
    post = get_object_or_404(Post, id = pk)
    post_room = get_object_or_404(Room, id = post.room.pk)
    friends_list = globalContext(request)["friends_list"]
    if post_room.host != request.user:
        if post_room.status == 1 and post_room.host not in friends_list:
            raise PermissionDenied
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.status = 1
            instance.post = post
            form.save()
            return redirect('home')
        
    context = {'form':form}
    return render(request, 'comments/comment_form.html', context)


@login_required(login_url='login')
def editComment(request, pk):
    comment = get_object_or_404(Comment, pk = pk)
    form = CommentForm(instance=comment)
    if comment.author != request.user:
        raise PermissionDenied
    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('home')
    
    context = {'form':form}
    return render(request, 'comments/comment_form.html', context)


@login_required(login_url='login')
def deleteComment(request, pk):
    comment = get_object_or_404(Comment, id = pk)
    room = comment.post.room.id
    if request.user == comment.author:
        if request.method == "POST":
            comment.delete()
            return redirect('room_id',room)
    else:
        raise PermissionDenied

    return render(request, 'delete.html', {'obj':comment})


@login_required(login_url='login')
def likeComment(request, pk):
    comment = get_object_or_404(Comment, id = pk)
    post = comment.post
    user = request.user
    room = post.room.id
    if user in comment.likes.all():
        comment.likes.remove(user)
    else:
        comment.likes.add(user)
    return redirect('room_id',room)


@login_required(login_url='login')
def dislikeComment(request, pk):
    comment = get_object_or_404(Comment, id = pk)
    post = comment.post
    user = request.user
    room = post.room.id
    if user in comment.dislikes.all():
        comment.dislikes.remove(user)
    else:
        comment.dislikes.add(user)
    return redirect('room_id',room)