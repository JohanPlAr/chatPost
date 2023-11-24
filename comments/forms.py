from django.forms import ModelForm
from .models import Comment

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        exclude = ('author','post','edited','status','likes','dislikes')