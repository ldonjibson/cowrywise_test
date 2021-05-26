
from django.contrib import admin
from django.urls import path
from .views import generate_uuid, main

app_name='uuid_app'
urlpatterns = [
    path('', main, name='main'),
    path('api/v1/', main, name='main'),
    path('api/v1/generate', generate_uuid, name='generate_uuid'),
]
