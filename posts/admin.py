from django.contrib import admin
from .models import Post, Comment


# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """Post model admin page configuration"""
    list_display = (
        'author',
      #  'room',
        'content',
        'edited',
        'created',
        'updated'
    )
    list_filter = ['author', 'edited']

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """Comment model admin page configuration"""
    list_display = (
        'author',
        'post',
        'content',
        'edited',
        'created',
        'updated'
    )
    list_filter = ['author', 'edited']