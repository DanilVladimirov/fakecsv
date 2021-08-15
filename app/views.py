from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import (render,
                              redirect)
from app.models import (Schema,
                        Column,
                        DataSet)
from app.services import (update_columns,
                          update_schema,
                          create_column)
from app.tasks import create_data_set


def start_page(request):
    template = 'app/schemas.html'
    context = {}
    action = request.POST.get('action')

    if request.POST and action == 'del':
        Schema.objects.get(id=request.POST.get('sid')).delete()

    schemas = Schema.objects.all()
    context.update({'schemas': schemas})

    return render(request, template, context)


@login_required
def create_schema(request):
    new_chema = Schema.objects.create(name='new_schema')

    return redirect('edit-schema-page', sid=new_chema.id)


@login_required
def edit_schema(request, sid):
    template = 'app/edit-schema.html'
    schema = Schema.objects.get(id=sid)
    columns = schema.column.all().order_by('order')
    action = request.POST.get('action')
    context = {}

    if request.POST and action == 'submit':
        update_columns(request)
        update_schema(request, schema)
        messages.success(request, 'saved !')

    if request.POST and action == 'add':
        create_column(request, schema)

    if request.POST and action == 'del':
        Column.objects.get(id=request.POST.get('cid')).delete()
        print(request.POST)

    context.update({'types': Column.TYPES,
                    'separators': Schema.SEPARATORS,
                    'schema': schema,
                    'columns': columns})

    return render(request, template, context)


@login_required
def generate_dataset_page(request, sid):
    template = 'app/generate_dataset.html'
    schema = Schema.objects.get(id=sid)
    columns = schema.column.all().order_by('order')

    if request.POST:
        rows = request.POST.get('rows')
        new_dataset = DataSet.objects.create(user=request.user)
        create_data_set.apply_async(args=(schema.id, int(rows), new_dataset.id))
        return redirect('datasets-page')

    context = {'schema': schema,
               'columns': columns}

    return render(request, template, context)


@login_required
def datasets_page(request):
    template = 'app/datasets.html'

    datasets = request.user.dataset_set.all().order_by('creation_date')

    context = {'datasets': datasets}

    return render(request, template, context)
