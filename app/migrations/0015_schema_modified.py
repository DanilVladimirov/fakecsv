# Generated by Django 3.2.6 on 2021-08-15 17:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_rename_status_creation_dataset_is_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='schema',
            name='modified',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
