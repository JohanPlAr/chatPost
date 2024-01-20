"""Friend Request Model"""
from django.db import models
from django.contrib.auth.models import User

STATUS = ((0, "Pending"), (1, "Accepted"))


class FriendRequest(models.Model):
    """Settings Friend Request Model"""
    sender = models.ForeignKey(
        User,
        related_name='outgoing_friend_requests',
        on_delete=models.CASCADE
    )
    receiver = models.ForeignKey(
        User,
        related_name='incoming_friend_requests',
        on_delete=models.CASCADE
    )
    created = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS)
