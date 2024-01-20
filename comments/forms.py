"""Comment Form Settings"""
from django.forms import ModelForm
from django import forms
from .models import Comment


class CommentForm(ModelForm):
    """Defines the Form for Comment Inputs"""
    class Meta:
        """Fields and widgets for CommentForm"""
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 4,
                                             'id': 'comment{{post}}',
                                             'maxlength': 300,
                                             'placeholder': 'Max 300 characters'},
                                      )
        }
