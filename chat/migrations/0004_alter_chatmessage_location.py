# Generated by Django 5.2 on 2025-05-01 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0003_remove_chatmessage_title_chatmessage_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chatmessage',
            name='location',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
