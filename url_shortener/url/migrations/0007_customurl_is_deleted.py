# Generated by Django 5.1 on 2024-08-22 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('url', '0006_customurl_one_time_only'),
    ]

    operations = [
        migrations.AddField(
            model_name='customurl',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
    ]
