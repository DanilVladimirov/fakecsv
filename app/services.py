from app.models import Column


def update_schema(request, schema):
    schema.name = request.POST.get('name')
    schema.separator = request.POST.get('separator')
    schema.save()


def update_columns(request):
    columns_dict = dict(request.POST)
    cids = columns_dict['cid']
    column_names = columns_dict['column_name']
    types = columns_dict['type']
    orders = columns_dict['order']
    ranges_from = columns_dict.get('from')
    ranges_to = columns_dict.get('to')
    print(request.POST)
    for i, cid in enumerate(cids):
        specific_range = {}
        if types[i] == 'integer':
            specific_range = {'from': ranges_from[i],
                              'to': ranges_to[i]}

        Column.objects.filter(id=cid).update(name=column_names[i],
                                             type=types[i],
                                             order=int(orders[i]),
                                             specific_range=specific_range)


def create_column(request, schema):
    c_name = request.POST.get('column_name')
    type_ = request.POST.get('type')
    order = request.POST.get('order')

    new_column = Column.objects.create(name=c_name,
                                       type=type_,
                                       order=order,
                                       schema=schema)
    if type_ == 'integer':
        new_column.specific_range = {'from': request.POST.get('from'),
                                     'to': request.POST.get('to')}
    new_column.save()
