# Generated by Django 3.0.3 on 2020-04-08 10:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0025_key_copykey'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='key',
            name='copykey',
        ),
        migrations.RemoveField(
            model_name='key',
            name='due_back',
        ),
    ]
