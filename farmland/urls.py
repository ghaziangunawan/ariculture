from django.urls import path
from farmland.views import show_farmland
from farmland.views import create_userland


app_name = 'farmland'

urlpatterns = [
    path('', show_farmland, name='show_farmland'),
    path('create/', create_userland, name='create_userland'),
]