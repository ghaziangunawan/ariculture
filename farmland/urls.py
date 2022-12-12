from django.urls import path
from farmland.views import *


app_name = 'farmland'

urlpatterns = [
    path('', show_farmland, name='show_farmland'),
    path('create/', create_userland, name='create_userland'),
    path('addland/', addland, name='addland'),
]