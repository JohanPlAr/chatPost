from django.urls import path
from . import views

urlpatterns = [
    path("list", views.friendsList, name='friends_list'),
    path("request/<int:pk>", views.friendRequest, name='friend_request'),
    path("accept/<int:pk>", views.accept_friend_request, name='accept_friend_request'),
    path('decline/<int:pk>',views.decline_friend_request, name='decline_friend_request'),
    path('remove/<int:pk>',views.remove_friend, name='remove_friend'),
    
]