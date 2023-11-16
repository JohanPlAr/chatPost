from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.loginView, name="login"),
    path("logout/", views.logoutUser, name="logout"),
]