# Generated by Django 3.0.3 on 2020-07-13 07:56

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('crazylab', '0006_auto_20200713_0936'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='apple',
            field=models.ManyToManyField(blank=True, related_name='apple_post', to=settings.AUTH_USER_MODEL),
        ),
    ]
