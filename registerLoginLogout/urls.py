from django.urls import path
from . import views

urlpatterns = [
    path("login", views.loginView, name="login"),
    path("logout/", views.logoutUser, name="logout"),
    path("register/", views.registerView, name="register"),
    path("profile/<int:pk>", views.createProfile, name='create_profile'),
    path("view-profile/<int:pk>", views.profileView, name='view_profile'),
   
]