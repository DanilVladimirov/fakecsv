# Generated by Django 3.2.6 on 2021-08-14 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_dataset'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schema',
            name='separator',
            field=models.CharField(choices=[(',', 'Comma (,)'), (';', 'semicolon (;)'), ('|', 'pipe (|)')], default='comma', max_length=12),
        ),
    ]
