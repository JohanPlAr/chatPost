from django.urls import path
from . import views

urlpatterns = [
    path("login", views.loginView, name="login"),
    path("logout/", views.logoutUser, name="logout"),
    path("register/", views.registerView, name="register"),
    path("profile/", views.createProfile, name='create_profile'),
]