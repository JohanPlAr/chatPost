from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from . forms import FriendRequestForm
from .models import FriendRequest

@login_required(login_url='login')
def friendRequest(request, pk):
    sender_id = request.user
    receiver_id = User.objects.get(id=pk)
    FriendRequest.objects.create(sender=sender_id, receiver=receiver_id, status=0)
    return redirect('home')

@login_required(login_url='login')
def friendsList(request):
    received_requests = FriendRequest.objects.filter(receiver=request.user)
    sent_requests = FriendRequest.objects.filter(sender=request.user)
    denied_requests = FriendRequest.objects.filter(receiver=request.user, status=2)
    context = {'sent_requests':sent_requests,'received_requests':received_requests, 'denied_requests':denied_requests}
    return render(request, 'friends/friends.html', context)

@login_required(login_url='login')
def accept_friend_request(request, pk):
    
    friend_request_id = FriendRequest.objects.get(pk=pk)
    friend_request_id.accept_friend_request(request.user)
    friend_data = FriendRequest.objects.all()
    context = {'friend_data':friend_data}
    return render(request, 'friends/friends.html', context)
