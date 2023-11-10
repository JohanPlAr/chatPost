from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


STATUS = ((0, "Draft"),(1, "Published"))

POST_TYPE = ((0, "public_wall"), (1, "room"))

class Post(models.Model):
    """ Post Model"""
    author = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='posts', null=True)
    content = models.TextField(max_length=550)
    edited = models.BooleanField(default=False)
    image = CloudinaryField('post-image', default='placeholder')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)
    post_type = models.IntegerField(choices=POST_TYPE)
    likes = models.ManyToManyField(User, related_name="post_like", blank= True)
    dislikes = models.ManyToManyField(User, related_name="post_dislike", blank= True)
    shares = models.ManyToManyField(User, related_name="post_share", blank= True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.content
    
    def number_of_likes(self):
        return self.likes.count()

    def number_of_dislikes(self):
        return self.dislikes.count()
    
    def number_of_shares(self):
        return self.shares.count()
    
    def get_comments(self):
        return self.comments.all()
    
class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='comments', null=True)
    post = models.ForeignKey(Post, on_delete=CASCADE, related_name='comments')
    content = models.TextField(max_length=550)
    edited = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(User, related_name="post_like", blank= True)
    dislikes = models.ManyToManyField(User, related_name="post_dislike", blank= True)

    class Meta:
        ordering = ['created_at']

        def __str__(self):
            return self.content
        
        def number_of_likes(self):
            return self.likes.count()

        def number_of_dislikes(self):
            return self.dislikes.count()
    
        def number_of_shares(self):
            return self.shares.count()
