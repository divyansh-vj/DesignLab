# Generated by Django 5.1.5 on 2025-04-10 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_alter_case_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='caseupdate',
            name='phone_number',
            field=models.CharField(default=1234567890, max_length=10),
            preserve_default=False,
        ),
    ]
