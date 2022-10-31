from django.urls import path, include
from advertisement.views import  show_advertisement
from advertisement.views import show_json




urlpatterns = [
    path('', show_advertisement, name='show_advertisement'),
    path('json/', show_json, name='show_json'),
]