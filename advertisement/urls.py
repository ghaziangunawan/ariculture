from django.urls import path, include
from . import views

app_name = 'advertisement'

urlpatterns = [
    path('', views.show_advertisement, name='show_advertisement'),
    path('json/', views.show_json, name='show_json'),
    path('Advertising/', views.show_advertisement_user, name='advertise'),
    path('Create_Advert/', views.create_ad, name='create_ad'),
    path("Advertising/set_remove/<int:id>", views.set_remove, name="set_remove"),
    path("json_user/", views.show_advertisement_json_per_user, name="show_advertisement_json_per_user"),    
    path("save_ad_f/", views.save_ad_f, name="save_ad_f"),
    path("set_remove_flutter/<int:id>", views.set_remove_flutter, name="set_remove_flutter"),  
]