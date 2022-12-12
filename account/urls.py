from django.urls import path
from account.views import *

app_name = 'account'

urlpatterns = [
    path('', account, name='account'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('profile/', profile, name='profile'),
    path('profile/json', show_profile_json, name='show_profile_json'),
    path("remove_land/<int:id>", remove_land, name="remove_land"),
    path('json/', show_json, name='show_json'),
    path('login_f/', login_f, name='login_f'),
    path('register_f/', register_f, name='register_f'),
    path('profile_f/<str:user>/', profile_json, name='profile_json'),
    path('logout_user_f/', logout_user_f, name='logout_user_f'),
    
]