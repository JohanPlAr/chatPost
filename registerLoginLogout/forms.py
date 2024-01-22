from django.forms import ModelForm
from .models import Profile
from cloudinary.forms import CloudinaryFileField
from django import forms



class ProfileForm(ModelForm):
    avatar = CloudinaryFileField(required=False)
    class Meta:
        model = Profile
        fields = ('bio','first_name','last_name','email','avatar')
        widgets = {
        'bio': forms.Textarea(attrs={'rows': 5, 'cols': 30, 'maxlength':500, 'placeholder':'Max 500 characters'}),
        }
    
    def __init__(self, *args, **kwargs):
       super().__init__(*args, **kwargs)
       self.fields['avatar'].options={
           'tags': 'avatar',
           'format': 'WebP',
            'crop': 'limit', 'width': 300, 'height': 300,
            'eager': [{ 'crop': 'fill', 'width': 300, 'height': 300,  'gravity': 'face' }]
                }
