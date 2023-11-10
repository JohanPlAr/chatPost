from django.contrib import admin
from .models import Post, Comment


# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """Post model admin page configuration"""
    list_display = (
        'author',
        'content',
        'post_type',
        'edited',
        'created_at',
        'updated_at'
    )
    list_filter = ['author', 'post_type', 'edited']

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """Comment model admin page configuration"""
    list_display = (
        'author',
        'post',
        'content',
        'edited',
        'created_at',
        'updated_at'
    )
    list_filter = ['author', 'edited']