from django.urls import path
from . import views



app_name = 'homepage'

urlpatterns = [
    path('', views.show_comment, name='index'),
    path('get/', views.get_comment, name='get_comment'),
    path('add/', views.add_comment, name='add_comment'),
    path('Advertising/', views.show_advertisement_user, name='advertise'),
    path('Create_Advert/', views.create_ad, name='create_ad'),
    path("Advertising/set_remove/<int:id>", views.set_remove, name="set_remove"),
    path("json/", views.show_json, name="show_json"),    
    path("save_ad_f/", views.save_ad_f, name="save_ad_f"),    
    path("set_remove_flutter/<int:id>", views.set_remove_flutter, name="set_remove_flutter"),  
    path("save_comment_f/", views.save_comment_f, name="save_comment_f")
]
