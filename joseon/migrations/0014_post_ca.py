# Generated by Django 3.0.3 on 2020-07-28 12:11

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('joseon', '0013_comment_nickname'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='ca',
            field=models.ManyToManyField(blank=True, related_name='comment_ca', to=settings.AUTH_USER_MODEL),
        ),
    ]
