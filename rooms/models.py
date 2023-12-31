from django.db import models
from django.contrib.auth.models import User

STATUS = ((0, "Public"),(1, "Friends Only"))


# Create your models here.
class Topic(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__ (self):
          return self.name

class Room(models.Model):
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=50)
    description = models.TextField(null=True, max_length=150, blank=True)
    status = models.IntegerField(choices=STATUS, default=0)
    participants = models.ManyToManyField(User, related_name='participants', blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
         ordering = ['-updated', '-created']

    def __str__(self):
        return self.name
    
    def number_of_posts(self):
        return self.post_room.count()