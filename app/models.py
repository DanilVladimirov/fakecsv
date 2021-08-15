from django.contrib.auth.models import User
from django.db import models
import datetime


def default_dict():
    return {}


class Column(models.Model):
    TYPES = (
        ('phone', 'phone number'),
        ('full_name', 'full name'),
        ('integer', 'integer'),
        ('email', 'email'),
        ('job', 'job'),
        ('address', 'address')
    )

    name = models.CharField(max_length=200, default='')
    type = models.CharField(choices=TYPES, max_length=12, default='phone')
    order = models.PositiveIntegerField(default=0)
    schema = models.ForeignKey('Schema', on_delete=models.CASCADE, related_name='column')
    specific_range = models.JSONField(default=default_dict)


class Schema(models.Model):
    SEPARATORS = (
        (',', 'Comma (,)'),
        (';', 'semicolon (;)'),
        ('|', 'pipe (|)')
    )

    name = models.CharField(max_length=200, default='')
    separator = models.CharField(choices=SEPARATORS, max_length=12, default='comma')

    def __str__(self):
        return f'schema #{self.id}'


class DataSet(models.Model):

    creation_date = models.DateField(default=datetime.date.today)
    is_created = models.BooleanField(default=False)
    file = models.FileField(null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, default=None)

    def __str__(self):
        return f'dataset #{self.id}'
