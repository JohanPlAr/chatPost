# Generated by Django 3.2.23 on 2023-11-28 23:26

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('registerLoginLogout', '0002_auto_20231128_2321'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='FriendRequests',
            new_name='FriendRequest',
        ),
        migrations.RenameModel(
            old_name='Profiles',
            new_name='Profile',
        ),
    ]
