from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import FriendRequest
from django.contrib import messages
from django.core.exceptions import PermissionDenied
from django.db.models import Q
from chatPost.context_processors import globalContext



@login_required(login_url='login')
def friendsList(request):
    if request.GET.get('q') is None:
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
    sender = request.user
    receiver = get_object_or_404(User.objects, id = pk)
    friends_list = globalContext(request)["friends_list"]
    if receiver not in friends_list:
        FriendRequest.objects.create(sender=sender, receiver=receiver, status=0)
    return redirect('friends_list')


@login_required(login_url='login')
def accept_friend_request(request, pk):
    friend_request = get_object_or_404(FriendRequest.objects, id = pk)
    friends_list = globalContext(request)["friends_list"]
    if friend_request.sender in friends_list:
        messages.error(f'{friend_request.sender} already in Friends-List')
    if friend_request.receiver == request.user:
        friend_request.status = 1
        friend_request.save()
    if friend_request.receiver != request.user:
        raise PermissionDenied
    return render(request, 'friends/friends.html')


@login_required(login_url='login')
def remove_friend(request, pk):
# Removes friendrequest and renders updated friendslist.
    friend_request = get_object_or_404(FriendRequest.objects, id = pk)
    if friend_request.receiver == request.user:
        friend_name = friend_request.sender
    elif friend_request.sender == request.user:
        friend_name = friend_request.receiver
    else:
        raise PermissionDenied
    if request.method == 'POST':
        friend_request.delete()
        return render(request, 'friends/friends.html')
    return render(request, 'delete.html', {'obj':friend_name})
