# Generated by Django 3.2.23 on 2024-01-25 13:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0002_alter_comment_content'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='status',
        ),
    ]
