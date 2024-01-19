"""Views for home page which displays a list of Rooms"""
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from rooms.models import Room



@login_required(login_url = 'login')
def home(request):
    """Manipulates context for render of rooms 
    on homepage and when searchbox is operated"""
    q = request.GET.get('q') if request.GET.get('q') is not None else ''
    rooms = Room.objects.filter(
        Q(topic__name__icontains=q) |
        Q(name__icontains=q) |
        Q(description__icontains=q) |
        Q(host__username__icontains=q)
                                )
    context = {'rooms':rooms}
    return render(request, 'base/home.html', context)
