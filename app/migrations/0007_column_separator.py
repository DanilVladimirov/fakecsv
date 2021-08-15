# Generated by Django 3.2.6 on 2021-08-14 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_alter_column_specific_range'),
    ]

    operations = [
        migrations.AddField(
            model_name='column',
            name='separator',
            field=models.CharField(choices=[('comma', 'Comma (,)'), ('semicolon', 'semicolon (;)'), ('pipe', 'pipe (|)')], default='comma', max_length=12),
        ),
    ]
