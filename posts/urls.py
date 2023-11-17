from django.urls import path, include
from . import views

urlpatterns = [
    path('edit/<str:pk>', views.editPost, name="edit_post"),
    path('create', views.createPost, name="create_post"),
    path('delete/<str:pk>', views.deletePost, name="delete_post"),
    path('comment/', include('comments.urls'), name='comment'),
    path('post_like/<str:pk>', views.likePost, name='like_post'),
    ]