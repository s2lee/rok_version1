# Generated by Django 3.0.3 on 2020-07-24 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0041_item_letter'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='impeachment',
            field=models.PositiveIntegerField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='reference_letter',
            field=models.PositiveIntegerField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='refutation',
            field=models.PositiveIntegerField(default=0, null=True),
        ),
    ]
