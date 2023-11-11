from django.urls import path, include
from . import views

urlpatterns = [
    path('edit/<str:pk>', views.editPost, name="edit_post"),
    path('create', views.createPost, name="create_post"),
    path('delete/<str:pk>', views.deletePost, name="delete_post"),     
    ]