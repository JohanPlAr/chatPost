from django.db import models
from django.contrib.auth.models import User

STATUS = ((0, "Pending"),(1, "Accepted"),(2, "Declined"))


class FriendRequest(models.Model):
    sender = models.ForeignKey(User, related_name='outgoing_friend_requests', on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name='incoming_friend_requests', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=(STATUS))

    def accept_friend_request(self, user):
        FriendRequest.objects.filter(
            receiver=user, status=0
        ).update(status=1)

    def decline_friend_request(self, user):
        FriendRequest.objects.filter(
            receiver=user, status=0
        ).update(status=2)

    def number_of_accepted(self, user):
        FriendRequest.objects.filter(receiver=user, status=1).count() + FriendRequest.objects.filter(sender=user, status=1).count()

