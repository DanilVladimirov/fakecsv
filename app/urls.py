from django.urls import path
from app.views import (datasets_page,
                       create_schema,
                       edit_schema,
                       start_page,
                       generate_dataset_page)

urlpatterns = [
    path('', start_page, name='start-page'),
    path('create-schema/', create_schema, name='create-schema-page'),
    path('edit-schema/<int:sid>/', edit_schema, name='edit-schema-page'),
    path('generate_dataset/<int:sid>/', generate_dataset_page, name='generate_dataset_page'),
    path('datasets/', datasets_page, name='datasets-page')
]
