from django.urls import path
from . import views

urlpatterns = [
    path('edit/<str:pk>', views.editComment, name="edit_comment"),
    path('create/<str:pk>', views.createComment, name="create_comment"),
    path('delete/<str:pk>', views.deleteComment, name="delete_comment"),     
    path('comment_like/<str:pk>', views.likeComment, name='like_comment'),
    path('comment_dislike/<str:pk>', views.dislikeComment, name='dislike_comment'),
    ]