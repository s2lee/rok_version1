# Generated by Django 3.0.3 on 2020-02-25 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reality', '0003_post_recommend'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={},
        ),
        migrations.AlterField(
            model_name='post',
            name='recommend',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
