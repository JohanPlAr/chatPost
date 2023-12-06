from django.forms import ModelForm
from .models import Profile



class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ('bio','first_name','last_name','email','avatar')
