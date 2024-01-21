from django.contrib import admin
from . models import Comment

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