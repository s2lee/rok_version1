# Generated by Django 3.0.3 on 2020-08-04 03:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0053_ranker_ranking'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ranker',
            name='ranking',
        ),
    ]
