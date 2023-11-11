from django.shortcuts import render, redirect
from . models import Post
from .forms import PostForm


# Create your views here.
def createPost(request):
    form = PostForm()
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        
    context = {'form':form}
    return render(request, 'posts/post_form.html', context)

def editPost(request, pk):
    post = Post.objects.get(id=pk)
    form = PostForm(instance=post)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('home')
    
    context = {'form':form}
    return render(request, 'posts/post_form.html', context)

def deletePost(request, pk):
    post = Post.objects.get(id=pk)
    if request.method == "POST":
        room.delete()
        return redirect('home')

    return render(request, 'rooms/delete.html', {'obj':post})