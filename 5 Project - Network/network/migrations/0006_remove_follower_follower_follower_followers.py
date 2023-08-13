# Generated by Django 4.2 on 2023-08-09 08:38

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0005_alter_follower_follower'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='follower',
            name='follower',
        ),
        migrations.AddField(
            model_name='follower',
            name='followers',
            field=models.ManyToManyField(blank=True, related_name='followers', to=settings.AUTH_USER_MODEL),
        ),
    ]
