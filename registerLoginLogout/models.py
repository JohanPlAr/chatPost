from  django import forms
from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


STATUS = ((0, "Pending"),(1, "Accepted"),(2, "Declined"))

class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.PROTECT, primary_key=True)
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    bio = models.TextField(max_length=500, null=True, blank=True)
    email = models.EmailField(max_length=254)
    avatar = CloudinaryField('avatar', default='https://res.cloudinary.com/ddurovnhl/image/upload/v1701246735/default_avatar_poro4z.png')


    def __str__(self):
        return self.user
    
from django.db import models

class FriendRequest(models.Model):
    sender = models.ForeignKey(User, related_name='outgoing_friend_requests', on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name='incoming_friend_requests', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=(STATUS))

    def accept_friend_request(self, user):
        FriendRequest.objects.filter(
            receiver=user, STATUS=0
        ).update(STATUS=1)

    def decline_friend_request(self, user):
        FriendRequest.objects.filter(
            receiver=user, STATUS=0
        ).update(STATUS=2)

    def number_of_accepted(self, user):
        FriendRequest.objects.filter(receiver=user, STATUS=1).count() + FriendRequest.objects.filter(sender=user, STATUS=1).count()
