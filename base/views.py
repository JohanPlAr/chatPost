from django.shortcuts import render
from django.views import View
from posts.models import Post, Comment

def home(request):
    return render(request, 'base/home.html')

def public_wall(request):
    posts= Post.objects.all()
    context = {'posts':posts,}
    return render(request, 'base/home.html')
