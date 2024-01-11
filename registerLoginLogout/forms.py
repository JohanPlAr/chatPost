from django.forms import ModelForm
from .models import Profile
from cloudinary.forms import CloudinaryFileField



class ProfileForm(ModelForm):
    avatar = CloudinaryFileField()
    class Meta:
        model = Profile
        fields = ('bio','first_name','last_name','email','avatar')
    
    def __init__(self, *args, **kwargs):
       super().__init__(*args, **kwargs)
       self.fields['avatar'].options={
           'tags': 'avatar',
           'format': 'WebP',
            'crop': 'limit', 'width': 300, 'height': 300,
            'eager': [{ 'crop': 'fill', 'width': 150, 'height': 100 }]
                }
