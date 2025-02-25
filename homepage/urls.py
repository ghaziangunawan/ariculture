from django.urls import path
from . import views



app_name = 'homepage'

urlpatterns = [
    path('', views.show_comment, name='index'),
    path('get/', views.get_comment, name='get_comment'),
    path('add/', views.add_comment, name='add_comment'),    
    path("save_comment_f/", views.save_comment_f, name="save_comment_f")
]
