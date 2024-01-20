"""Url patterns for comments crud views"""
from django.urls import path
from . import views

urlpatterns = [
    path('edit/<str:pk>', views.edit_comment, name="edit_comment"),
    path('create/<str:pk>', views.create_comment, name="create_comment"),
    path('delete/<str:pk>', views.delete_comment, name="delete_comment"),
    path('comment_like/<str:pk>', views.like_comment, name='like_comment'),
    path('comment_dislike/<str:pk>', views.dislike_comment, name='dislike_comment'),
]
