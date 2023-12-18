from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from . forms import ProfileForm
from . models import Profile
from friends.models import FriendRequest

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
def createProfile(request):
    form = ProfileForm
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
    context = {'profiles':profiles, "f_profile_sender":f_profile_sender, 'f_profile_receiver':f_profile_receiver}
    return render(request, 'registerLoginLogout/profile.html', context)