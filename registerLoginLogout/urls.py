from django.urls import path, include
from . import views

urlpatterns = [
    path("login", views.loginView, name="login"),
    path("logout/", views.logoutUser, name="logout"),
    path("register/", views.registerView, name="register"),
]