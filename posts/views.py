from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . models import Post
from rooms.models import Room
from .forms import PostForm
from cloudinary import CloudinaryResource


 


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
            json_response = { "public_id": "test" }
            # Populate CloudinaryResource object using the upload response
            result = CloudinaryResource(public_id=json_response['public_id'])
            instance.image = result.get_prep_value()                
            input(result)
            instance.room.participants.add(request.user)
            return redirect('room_id', post_room.id)
        
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
            instance = form.save(commit=False)
            instance.edited = True
            form.save()
            return redirect('home')
    
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