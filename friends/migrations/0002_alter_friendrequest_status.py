# Generated by Django 3.2.23 on 2024-01-11 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('friends', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='friendrequest',
            name='status',
            field=models.IntegerField(choices=[(0, 'Pending'), (1, 'Accepted')]),
        ),
    ]