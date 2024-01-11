from django.shortcuts import render
from django.db.models import Q
from rooms.models import Room
from django.contrib.auth.decorators import login_required


@login_required(login_url = 'login')
def home(request):

    q = request.GET.get('q') if request.GET.get('q') != None else ''
    rooms = Room.objects.filter(
        Q(topic__name__icontains=q) |
        Q(name__icontains=q) |
        Q(description__icontains=q) |
        Q(host__username__icontains=q)
                                )
    context = {'rooms':rooms}
    return render(request, 'base/home.html', context)

    
