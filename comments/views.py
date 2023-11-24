from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from . models import Comment
from posts.models import Post
from .forms import CommentForm


# Create your views here.

@login_required(login_url='login')
def createComment(request, pk):
    form = CommentForm()
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.status = 1
            instance.post = Post.objects.get(id=pk)
            form.save()
            return redirect('home')
        
    context = {'form':form}
    return render(request, 'comments/comment_form.html', context)

@login_required(login_url='login')
def editComment(request, pk):
    comment =Comment.objects.get(id=pk)
    form = CommentForm(instance=comment)
    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('home')
    
    context = {'form':form}
    return render(request, 'comments/comment_form.html', context)

@login_required(login_url='login')
def deleteComment(request, pk):
    comment =Comment.objects.get(id=pk)
    if request.method == "POST":
        comment.delete()
        return redirect('home')

    return render(request, 'rooms/delete.html', {'obj':comment})

@login_required(login_url='login')
def likeComment(request, pk):
    comment = Comment.objects.get(id=pk)
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
    comment = Comment.objects.get(id=pk)
    post = comment.post
    user = request.user
    room = post.room.id
    if user in comment.dislikes.all():
        comment.dislikes.remove(user)
    else:
        comment.dislikes.add(user)
    return redirect('room_id',room)