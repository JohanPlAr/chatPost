from django.contrib import admin
from . models import Room, Topic

# Register your models here.
@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    """Room model admin page configuration"""
    list_display = (
    'host',
    'topic',
    'name',  
    'description',    
    'status',
    'updated',
    'created',  
    )
    list_filter = ['host', 'topic', 'name']


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    """Topic model admin page configuration"""
    list_display = (
   'name', 
    )
    list_filter = ['name']