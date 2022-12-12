from django.urls import path
from news.views import show_news, get_feedback, add_feedback, delete_task,show_json,save_review,delete_flutter

app_name = 'news'

urlpatterns = [
    path('', show_news, name='news'),
    path('get/', get_feedback, name='get_feedback'),
    path('add/', add_feedback, name='add_feedback'),
    path('delete/<int:id>', delete_task, name='delete_task'),
    path('json/', show_json, name='show_json'),
    path("save_review/", save_review, name="save_review"),
    path('delete_flutter/<int:id>', delete_flutter, name='delete_flutter'),
    ]