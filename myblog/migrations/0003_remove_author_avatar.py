# Generated by Django 3.2 on 2022-02-07 18:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0002_auto_20220207_2117'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='avatar',
        ),
    ]
