from django.shortcuts import render, redirect, HttpResponse
from . forms import RoomForm

# Create your views here.
def createRoom(request):
    form = RoomForm()
    if request.method == "POST":
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        
    context = {'form':form}
    return render(request, 'rooms/room_form.html', context)
