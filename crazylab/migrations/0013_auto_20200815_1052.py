# Generated by Django 3.0.3 on 2020-08-15 01:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crazylab', '0012_auto_20200813_2308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='text',
            field=models.TextField(max_length=300),
        ),
        migrations.AlterField(
            model_name='post',
            name='contents',
            field=models.TextField(max_length=1400),
        ),
    ]
