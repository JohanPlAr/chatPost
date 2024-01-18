from django.forms import ModelForm
from .models import Room
from django import forms

class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = ('topic','name','description','description','status')
        widgets = {
        'description': forms.Textarea(attrs={
                                             'rows': 4, 
                                             'cols': 40, 
                                             'maxlength':150, 
                                             'placeholder':'Max 150 characters'
                                             }),
        }