# Generated by Django 3.2.23 on 2024-01-11 10:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0007_alter_post_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='shares',
        ),
    ]
