from django.db import models
from django.contrib.auth.models import User
from django.db.models import Q

STATUS = ((0, "Pending"),(1, "Accepted"))


class FriendRequest(models.Model):
    sender = models.ForeignKey(User, related_name='outgoing_friend_requests', on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name='incoming_friend_requests', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=(STATUS))

    def accept_friend_request(self, user):
        FriendRequest.objects.filter(
            receiver=user, status=0
        ).update(status=1)