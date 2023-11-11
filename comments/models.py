from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from posts.models import Post

STATUS = ((0, "Draft"),(1, "Published"))

# Create your models here.
class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='commentsAuthor', null=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='commentsPost')
    content = models.TextField(max_length=550)
    edited = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(User, related_name="comment_like", blank= True)
    dislikes = models.ManyToManyField(User, related_name="comment_dislike", blank= True)

    class Meta:
        ordering = ['created']

    def __str__(self):
        return self.content
    
    def number_of_likes(self):
        return self.likes.count()

    def number_of_dislikes(self):
        return self.dislikes.count()