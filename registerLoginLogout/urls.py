"""Patterns for profile and authentication urls"""
from django.urls import path
from . import views

urlpatterns = [
    path("login", views.login_view, name="login"),
    path("logout/", views.logout_user, name="logout"),
    path("register/", views.register_view, name="register"),
    path("profile/<int:pk>", views.create_profile, name='create_profile'),
    path("view-profile/<int:pk>", views.profile_view, name='view_profile'),

]
