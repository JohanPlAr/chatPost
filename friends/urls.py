"""Patterns for Profile view and Friend Request crud Url:S"""
from django.urls import path
from registerLoginLogout import views as profile
from . import views


urlpatterns = [
    path("list", views.friends_list_view, name='friends_list'),
    path("request/<int:pk>", views.friend_request_view, name='friend_request'),
    path("accept/<int:pk>", views.accept_friend_request,
         name='accept_friend_request'),
    path('remove/<int:pk>', views.remove_friend, name='remove_friend'),
    path("view-profile/<int:pk>", profile.profile_view, name='view_profile'),
]
