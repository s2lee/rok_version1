# Generated by Django 3.0.3 on 2020-08-14 01:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reality', '0013_user_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='last_submit',
            field=models.DateField(auto_now=True, null=True),
        ),
    ]
