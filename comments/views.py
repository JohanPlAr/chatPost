"""Comment Crud, Like and Dislike functions"""

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from chatPost.context_processors import global_context
from posts.models import Post
from rooms.models import Room
from . models import Comment
from .forms import CommentForm



@login_required(login_url='login')
def create_comment(request, pk):
    """Create Comment function"""
    form = CommentForm()
    post = get_object_or_404(Post, id=pk)
    post_room = get_object_or_404(Room, id=post.room.pk)
    friends_list = global_context(request)["friends_list"]
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
            return redirect('room_id', post_room.id)

    context = {'form': form}
    return render(request, 'comments/comment_form.html', context)


@login_required(login_url='login')
def edit_comment(request, pk):
    """Handles Editting of comments"""
    comment = get_object_or_404(Comment, pk=pk)
    room = comment.post.room.id
    form = CommentForm(instance=comment)
    if comment.author != request.user:
        raise PermissionDenied
    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('room_id', room)

    context = {'form': form}
    return render(request, 'comments/comment_form.html', context)


@login_required(login_url='login')
def delete_comment(request, pk):
    """Handles delete comment requests"""
    comment = get_object_or_404(Comment, id=pk)
    room = comment.post.room.id
    if request.user == comment.author:
        if request.method == "POST":
            comment.delete()
            return redirect('room_id', room)
    else:
        raise PermissionDenied

    return render(request, 'delete.html', {'obj': comment})


@login_required(login_url='login')
def like_comment(request, pk):
    """Handles Like Comment"""
    comment = get_object_or_404(Comment, id=pk)
    post = comment.post
    user = request.user
    room = post.room.id
    if user in comment.likes.all():
        comment.likes.remove(user)
    else:
        comment.likes.add(user)
    return redirect('room_id', room)


@login_required(login_url='login')
def dislike_comment(request, pk):
    """Handles Dislike Comment"""
    comment = get_object_or_404(Comment, id=pk)
    post = comment.post
    user = request.user
    room = post.room.id
    if user in comment.dislikes.all():
        comment.dislikes.remove(user)
    else:
        comment.dislikes.add(user)
    return redirect('room_id', room)
