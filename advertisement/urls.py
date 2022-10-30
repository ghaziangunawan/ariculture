from django.urls import path
from advertisement.views import show_advertisement
from advertisement.views import show_json


app_name = 'advertisements'

urlpatterns = [
    path('', show_advertisement, name='show_advertisement'),
    path('json/', show_json, name='show_json'),
]