# Generated by Django 2.1.7 on 2019-04-08 09:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0008_auto_20190407_1432'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='comment_count',
        ),
    ]