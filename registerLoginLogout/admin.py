from django.contrib import admin
from . models import Profile

@admin.register(Profile)
class ProfilesAdmin(admin.ModelAdmin):
    """Profile model admin page configuration"""
    list_display = (
    'user', 
    'first_name',
    'last_name',
    'bio',
    'email',
    'avatar',
    )
    list_filter = ['user', 'email', 'bio']
