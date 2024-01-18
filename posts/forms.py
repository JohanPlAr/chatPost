from django.forms import ModelForm
from django import forms
from .models import Post
from cloudinary.forms import CloudinaryFileField


class PostForm(ModelForm):
    image = CloudinaryFileField()
    class Meta:
        model = Post
        fields = ('content', 'image')
        exclude = ('author','edited','status','likes','dislikes','shares', 'room')
        widgets = {
        'content': forms.Textarea(attrs={'rows': 5, 'cols': 20, 'maxlength':500, 'placeholder':'Max 500 characters'}),
        }
    def __init__(self, *args, **kwargs):
       super().__init__(*args, **kwargs)
       self.fields['image'].options={
           'tags': 'post-image',
           'format': 'WebP',
            'crop': 'limit', 'width': 500, 'height': 500,
            'eager': [{ 'crop': 'fill', 'width': 300, 'height': 200 }]
                }
