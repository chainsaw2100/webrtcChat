# Generated by Django 3.2 on 2021-12-30 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0007_rename_is_ip_and_mac_correct_profile_is_ip_correct'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='useragent',
        ),
        migrations.AddField(
            model_name='profile',
            name='first',
            field=models.BooleanField(default=False),
        ),
    ]
