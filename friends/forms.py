"""Friend Request ModelForm"""
from django.forms import ModelForm
from .models import FriendRequest


class FriendRequestForm(ModelForm):
    """Friend Request Form"""
    class Meta:
        """Define Friend Request Form"""
        model = FriendRequest
        fields = '__all__'
