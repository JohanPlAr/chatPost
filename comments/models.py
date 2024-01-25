"""Comment Model"""

from django.db import models
from django.contrib.auth.models import User
from posts.models import Post

class Comment(models.Model):
    """Comment Model """
    author = models.ForeignKey(User, on_delete=models.SET_NULL,
                               related_name='commentsAuthor',
                               null=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='commentsPost')
    content = models.TextField(max_length=200)
    edited = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(User, related_name="comment_like", blank=True)
    dislikes = models.ManyToManyField(User, related_name="comment_dislike", blank=True)

    class Meta:
        """Orders the comments with 
        last created in the bottom of the list"""
        ordering = ['created']

    def __str__(self):
        """Returns the content when comment is called"""
        return self.content

    def number_of_likes(self):
        """Returns number of likes"""
        return self.likes.count()

    def number_of_dislikes(self):
        """Returns number of dislikes"""
        return self.dislikes.count()
 