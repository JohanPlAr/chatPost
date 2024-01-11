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
        'content': forms.Textarea(attrs={'rows': 4, 'cols': 40}),
        }
    def __init__(self, *args, **kwargs):
       super().__init__(*args, **kwargs)
       self.fields['image'].options={
           'tags': 'post-image',
           'format': 'WebP',
            'crop': 'limit', 'width': 500, 'height': 500,
            'eager': [{ 'crop': 'fill', 'width': 150, 'height': 100 }]
                }
