# Generated by Django 3.2.6 on 2021-08-15 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_dataset_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dataset',
            name='status_creation',
            field=models.BooleanField(default=False),
        ),
    ]
