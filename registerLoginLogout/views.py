"""Authentication and Profile views"""
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.core.exceptions import PermissionDenied
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from friends.models import FriendRequest
from chatPost.context_processors import global_context
from . forms import ProfileForm
from . models import Profile



def loginView(request):
    """Renders Login Page and let's user log in on POST"""
    page = 'login'
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f"{user} is signed in")
            return redirect('home')
        else:
            messages.error(request, "Username or Password does not exist")
    context = {'page': page}
    return render(request, 'base/register_login.html', context)


def logoutUser(request):
    """Logs out user and Redirects to Login Page"""
    messages.success(request, f'{request.user} is logged out')
    logout(request)
    return redirect('login')


def registerView(request):
    """Renders register display, register form on 
    Post and creates a Profile Object"""
    page = 'register'
    form = UserCreationForm
    context = {'page': page, 'form': form, }

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            Profile.objects.create(user=user)
            login(request, user)
            messages.success(
                request,
                f'User {user.username} created successfully'
            )
            return redirect('home')
        else:
            messages.error(request, form.errors)
    return render(request, 'base/register_login.html', context)


@login_required(login_url='login')
def createProfile(request, pk):
    """Renders 'Manage Profile' display 
    and takes form input on POST"""
    profile = get_object_or_404(Profile.objects, user_id=pk)
    if request.user != profile.user:
        raise PermissionDenied
    form = ProfileForm(instance=profile)
    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            if "default_avatar" in str(instance.avatar):
                instance.avatar = profile.avatar.url
            instance.save()
            messages.success(request, 'Profile saved successfully')
            return redirect('view_profile', request.user.pk)
        else:
            messages.error(request, form.errors)
    context = {'form': form, 'profile': profile}
    return render(
        request,
        'registerLoginLogout/create_profile.html',
        context)


@login_required(login_url='login')
def profileView(request, pk):
    """Renders profile.html"""
    profile = get_object_or_404(Profile.objects, user_id=pk)
    friends_list = global_context(request)["friends_list"]
    received_requests = global_context(request)["received_requests"]
    sent_requests = global_context(request)["sent_requests"]
    if FriendRequest.objects.filter(
                sender=profile.user, receiver=request.user
            ):
        friend_request = FriendRequest.objects.get(
                sender=profile.user, receiver=request.user
            )
    if FriendRequest.objects.filter(
                sender=request.user, receiver=profile.user
            ):
        friend_request = FriendRequest.objects.get(
                sender=request.user, receiver=profile.user
            )
    else:
        friend_request = profile

    context = {
        'profile': profile,
        'friend_request': friend_request,
        'friends_list': friends_list,
        'received_requests': received_requests,
        'sent_requests': sent_requests
    }
    return render(
        request,
        'registerLoginLogout/profile.html',
        context
    )
