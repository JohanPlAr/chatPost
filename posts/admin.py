"""Sets Post Model in Admin panel"""
from django.contrib import admin
from .models import Post


# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """Post model admin page configuration"""
    list_display = (
        'author',
        'content',
        'edited',
        'created',
        'updated',
    )
    list_filter = ['author', 'edited']
