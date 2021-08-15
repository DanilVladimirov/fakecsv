import os
import random
from app.models import (DataSet,
                        Schema)
from fakecsv.celery import app
import csv
from faker import Faker
from os.path import join
from fakecsv import settings
from django.core.files.storage import default_storage


def file_random_path(filename):
    basefilename, file_extension = os.path.splitext(filename)
    chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890'
    randomstr = ''.join((random.choice(chars)) for x in range(10))
    return f'{basefilename}_{randomstr}{file_extension}'


def generate_csv(schema, rows):

    columns = schema.column.all().order_by('order')
    fake = Faker()
    file_name = file_random_path('data-set.csv')
    path = join(settings.MEDIA_ROOT, file_name)

    with open(path, mode="w") as csv_file:
        fields = [x.name for x in columns]
        writer = csv.writer(csv_file, delimiter=schema.separator)
        writer.writerow(fields)
        for i in range(rows):
            list_ = []
            for column in columns:
                if column.type == 'full_name':
                    list_.append(fake.name())
                if column.type == 'phone':
                    list_.append(fake.phone_number())
                if column.type == 'integer':
                    list_.append(random.randint(int(column.specific_range.get('from')),
                                                int(column.specific_range.get('to'))))
                if column.type == 'email':
                    list_.append(fake.email())
                if column.type == 'job':
                    list_.append(fake.job())
                if column.type == 'address':
                    list_.append(fake.address())
            writer.writerow(list_)
    return file_name


@app.task
def create_data_set(sid, rows, did):
    dataset = DataSet.objects.filter(id=did)
    schema = Schema.objects.get(id=sid)

    file_name = generate_csv(schema, rows)
    file = open('media/' + file_name, 'rb')
    default_storage.save(file_name, file)
    dataset.update(file=default_storage.url(file_name), is_created=True)

    return f'generated dataset'
