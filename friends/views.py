from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import FriendRequest

@login_required(login_url='login')
def friendRequest(request, pk):
# Handles friend request
    sender_id = request.user
    receiver_id = User.objects.get(id=pk)

    # Checks if receiver already exists in previous requests 
    all_requests = FriendRequest.objects.all()
    for instance in all_requests:
        if receiver_id == instance.sender and instance.receiver == sender_id:
            if instance.status == 0:
                return HttpResponse('Already friends')
            if instance.status == 1:
                return HttpResponse('You are already friends')
            if instance.status == 2:
                return HttpResponse('Request already been sent. Send again?')
    if sender_id == receiver_id:
        return HttpResponse("You can't friend yourself")
    FriendRequest.objects.create(sender=sender_id, receiver=receiver_id, status=0)
    return redirect('home')

@login_required(login_url='login')
def friendsList(request):
    friends_list =[]
    all_requests = FriendRequest.objects.all()
    received_requests = FriendRequest.objects.filter(receiver=request.user, status=0)
    sent_requests = FriendRequest.objects.filter(sender=request.user, status=0)
    denied_requests = FriendRequest.objects.filter(receiver=request.user, status=2)
    accepted_received_requests = FriendRequest.objects.filter(receiver=request.user, status=1)
    accepted_sent_requests = FriendRequest.objects.filter(sender=request.user, status=1)
    number_of_friends = accepted_received_requests.count() + accepted_sent_requests.count()
    for instance in accepted_sent_requests:
        friends_list.append(instance.receiver)
    for instance in accepted_received_requests:
        friends_list.append(instance.sender)
    context = {
        'all_requests':all_requests,
        'friends_list':friends_list,
        'number_of_friends':number_of_friends,
        'sent_requests':sent_requests,
        'received_requests':received_requests,
        'denied_requests':denied_requests
               }
    return render(request, 'friends/friends.html', context)

@login_required(login_url='login')
def accept_friend_request(request, pk):
    
    friend_request_id = FriendRequest.objects.get(pk=pk)
    friend_request_id.accept_friend_request(request.user)
    friend_data = FriendRequest.objects.all()
    context = {'friend_data':friend_data}
    return render(request, 'friends/friends.html', context)

@login_required(login_url='login')
def decline_friend_request(request, pk):
    
    friend_request_id = FriendRequest.objects.get(pk=pk)
    friend_request_id.decline_friend_request(request.user)
    friend_data = FriendRequest.objects.all()
    context = {'friend_data':friend_data}
    return render(request, 'friends/friends.html', context)

def remove_friend(request, pk):
    friend = FriendRequest.objects.get(pk=pk)
    if request.method == 'POST':
        friend.delete()

    return render(request, 'friends/friends.html')
