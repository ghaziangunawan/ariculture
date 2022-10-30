from django.urls import path
from homepage.views import index, show_json
from homepage.views import show_advertisement_user, create_ad, set_remove


app_name = 'homepage'

urlpatterns = [
    path('', index, name='index'),
    path('Advertising/', show_advertisement_user, name='advertise'),
    path('Create_Advert/', create_ad, name='create_ad'),
    path("set_remove/<int:id>", set_remove, name="set_remove"),
    path("json/", show_json, name="show_json"),    
]