from django.urls import path
from news.views import show_news,register,login_user,logout_user, get_feedback,add_feedback,delete_task

app_name = 'news'

urlpatterns = [
    path('', show_news, name='news'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('get/', get_feedback, name='get_feedback'),
    path('add/', add_feedback, name='add_feedback'),
    path('delete/<int:id>', delete_task, name='delete_task'),
    ]