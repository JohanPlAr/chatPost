"""Patterns for Posts crud Urls"""
from django.urls import path, include
from . import views

urlpatterns = [
    path('create/<str:pk>', views.createPost, name="create_post"),
    path('edit/<str:pk>', views.editPost, name="edit_post"),
    path('delete/<str:pk>', views.deletePost, name="delete_post"),
    path('comment/', include('comments.urls'), name='comment'),
    path('post-like/<str:pk>', views.likePost, name='like_post'),
    path('post-dislike/<str:pk>', views.dislikePost, name='dislike_post'),
]
