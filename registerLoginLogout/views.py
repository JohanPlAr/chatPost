from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from . forms import ProfileForm
from . models import Profile
from friends.models import FriendRequest
from rooms.models import Room

# Create your views here.

def loginView(request):
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
    context = {'page':page}
    return render(request, 'base/register_login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('home')

def registerView(request):
    page = 'register'
    form = UserCreationForm
    context = {'page':page, 'form':form,}

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            Profile.objects.create(user=user)
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, form.errors)
    return render(request, 'base/register_login.html', context)

@login_required(login_url='login')
def createProfile(request, pk):
    profile = Profile.objects.get(user_id=pk)
    form = ProfileForm(instance=profile)
    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            return redirect('home')
        else:
            messages.error(request, form.errors)
    context = {'form':form,}
    return render(request, 'registerLoginLogout/create_profile.html', context
)

def profileView(request, pk):
    profiles = Profile.objects.all()
    f_request = FriendRequest.objects.get(pk=pk)
    f_profile_sender = Profile.objects.get(pk=f_request.sender.pk)
    f_profile_receiver = Profile.objects.get(pk=f_request.receiver.pk)
    rooms = Room.objects.all()
    context = {'profiles':profiles,
               "f_profile_sender":f_profile_sender, 
               'f_profile_receiver':f_profile_receiver,
               'rooms':rooms
               }
    return render(request, 'registerLoginLogout/profile.html', context)

def new(request, pk):
    profile = Profile.objects.get(user_id=pk)
    friends_list =[]
    received_requests = []
    sent_requests = []
    rooms = Room.objects.all()
    accepted_received_requests = FriendRequest.objects.filter(receiver=request.user, status=1)
    for instance in accepted_received_requests:
        friends_list.append(instance.sender)
    accepted_sent_requests = FriendRequest.objects.filter(sender=request.user, status=1)
    for instance in accepted_sent_requests:
        friends_list.append(instance.receiver)
    pending_received_requests = FriendRequest.objects.filter(receiver=request.user, sender=pk, status=0)
    for instance in pending_received_requests:
        received_requests.append(instance)
    pending_sent_requests = FriendRequest.objects.filter(sender=request.user, receiver=pk, status=0)
    for instance in pending_sent_requests:
        sent_requests.append(instance)
    context = {'profile':profile,
               'friends_list':friends_list,
               'rooms':rooms,
               'received_requests':received_requests,
               'sent_requests':sent_requests}
    return render(request, 'registerLoginLogout/all_profiles.html', context)