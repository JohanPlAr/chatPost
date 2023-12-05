from django.contrib import admin
from . models import FriendRequest

@admin.register(FriendRequest)
class FriendRequestsAdmin(admin.ModelAdmin):
    """Profile model admin page configuration"""
    list_display = (
        'sender',
        'receiver',
        'status',
    )
   # Register your models here.