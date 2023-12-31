# Generated by Django 3.2.23 on 2023-11-23 08:47

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_alter_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=cloudinary.models.CloudinaryField(default='https://res.cloudinary.com/ddurovnhl/image/upload/v1700729202/samples/l83wf54aeup6jmn0xbou.png', max_length=255, verbose_name='post-image'),
        ),
    ]
