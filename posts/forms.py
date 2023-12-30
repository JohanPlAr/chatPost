from django.forms import ModelForm
from django import forms
from .models import Post


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ('content', 'image')
        exclude = ('author','edited','status','likes','dislikes','shares', 'room')
        widgets = {
        'content': forms.Textarea(attrs={'rows': 4, 'cols': 40}),
        }

