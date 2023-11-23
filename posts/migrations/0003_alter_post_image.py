# Generated by Django 3.2.23 on 2023-11-22 14:01

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_delete_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=cloudinary.models.CloudinaryField(default='media/social-media-post.jpg', max_length=255, verbose_name='post-image'),
        ),
    ]
