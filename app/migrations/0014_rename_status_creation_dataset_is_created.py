# Generated by Django 3.2.6 on 2021-08-15 11:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_alter_dataset_status_creation'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dataset',
            old_name='status_creation',
            new_name='is_created',
        ),
    ]
