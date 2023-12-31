from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import FriendRequest
from registerLoginLogout.models import Profile
from django.db.models import Q



@login_required(login_url='login')
def friendsList(request):
    if request.GET.get('q') == None:
        user_search = []
    else:
        q = request.GET.get('q')
        user_search = User.objects.filter(
            Q(username__icontains=q)
                                )
    context = {'user_search': user_search}
    
    return render(request, 'friends/friends.html', context)


@login_required(login_url='login')
def friendRequest(request, pk):
# Handles friend request
    sender_id = request.user
    receiver_id = User.objects.get(id=pk)            
    FriendRequest.objects.create(sender=sender_id, receiver=receiver_id, status=0)
    return redirect('friends_list')

@login_required(login_url='login')
def accept_friend_request(request, pk):
    
    friend_request_id = FriendRequest.objects.get(pk=pk)
    friend_request_id.accept_friend_request(request.user)
    return render(request, 'friends/friends.html')

def remove_friend(request, pk):
    friend = FriendRequest.objects.get(pk=pk)
    if friend.receiver == request.user:
        friend_name = friend.sender
    else:
        friend_name = friend.receiver
    if request.method == 'POST':
        friend.delete()
        return render(request, 'friends/friends.html')
    return render(request, 'delete.html', {'obj':friend_name})
