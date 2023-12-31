from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from rooms.models import Room

STATUS = ((0, "Draft"),(1, "Published"))


class Post(models.Model):
    """ Post Model"""
    author = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='posts', null=True)
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='post_room', default=False)
    content = models.TextField(max_length=550)
    edited = models.BooleanField(default=False)
    image = CloudinaryField('post-image', default='https://res.cloudinary.com/ddurovnhl/image/upload/v1700729202/samples/l83wf54aeup6jmn0xbou.png')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(User, related_name="post_like", blank= True)
    dislikes = models.ManyToManyField(User, related_name="post_dislike", blank= True)

    class Meta:
        ordering = ["-created"]

    def __str__(self):
        return self.content
    
    def number_of_likes(self):
        return self.likes.count()

    def number_of_dislikes(self):
        return self.dislikes.count()
    
    def number_of_comments(self):
        return self.commentsPost.count()
    
    def post_image(self):
        return self.image
