from django.forms import ModelForm
from .models import FriendRequest

class FriendRequestForm(ModelForm):
    class Meta:
        model = FriendRequest
        fields = '__all__'
        widgets = {
        'content': forms.Textarea(attrs={'rows': 4, 'cols': 40}),
        }