# Generated by Django 5.2 on 2025-04-24 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_alter_chatmessage_location'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chatmessage',
            name='title',
        ),
        migrations.AddField(
            model_name='chatmessage',
            name='username',
            field=models.CharField(default='anonymous', max_length=100),
        ),
    ]
