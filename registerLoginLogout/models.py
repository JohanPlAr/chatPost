from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.PROTECT, primary_key=True)
    first_name = models.CharField(max_length=50, default='user')
    last_name = models.CharField(max_length=50, default='last-name')
    bio = models.TextField(max_length=500, null=True, blank=True)
    email = models.EmailField(max_length=254)
    avatar = CloudinaryField(
        'avatar', 
        default='https://res.cloudinary.com/ddurovnhl/image/upload/v1701246735/default_avatar_poro4z.png'
        )