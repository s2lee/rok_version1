# Generated by Django 3.0.3 on 2020-05-20 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0038_remove_key_keystock'),
    ]

    operations = [
        migrations.AddField(
            model_name='userkey',
            name='OPCseventhkey',
            field=models.PositiveIntegerField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='userkey',
            name='OPCsixthkey',
            field=models.PositiveIntegerField(default=0, null=True),
        ),
    ]
