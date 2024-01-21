"""Patterns for Posts crud Urls"""
from django.urls import path, include
from . import views

urlpatterns = [
    path('create/<str:pk>', views.create_post, name="create_post"),
    path('edit/<str:pk>', views.edit_post, name="edit_post"),
    path('delete/<str:pk>', views.delete_post, name="delete_post"),
    path('comment/', include('comments.urls'), name='comment'),
    path('post-like/<str:pk>', views.like_post, name='like_post'),
    path('post-dislike/<str:pk>', views.dislike_post, name='dislike_post'),
]
