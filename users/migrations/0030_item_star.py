# Generated by Django 3.0.3 on 2020-04-15 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0029_item_getsword'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='star',
            field=models.PositiveIntegerField(default=0, null=True),
        ),
    ]