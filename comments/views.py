from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from . models import Comment
from .forms import CommentForm


# Create your views here.
def createComment(request):
    form = CommentForm()
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        
    context = {'form':form}
    return render(request, 'comments/comment_form.html', context)

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

def deleteComment(request, pk):
    comment =Comment.objects.get(id=pk)
    if request.method == "POST":
        comment.delete()
        return redirect('home')

    return render(request, 'rooms/delete.html', {'obj':comment})