from django.urls import path
from . import views

urlpatterns = [
    path('edit/<str:pk>', views.editComment, name="edit_comment"),
    path('create', views.createComment, name="create_comment"),
    path('delete/<str:pk>', views.deleteComment, name="delete_comment"),     
    ]