from django.forms import ModelForm
from cloudinary.forms import CloudinaryFileField
from .models import Post


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ('content', 'image')
        exclude = ('author','edited','status','likes','dislikes','shares', 'room')

