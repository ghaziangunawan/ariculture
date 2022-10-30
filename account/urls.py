from django.urls import path
from account.views import *

app_name = 'account'

urlpatterns = [
    path('', account, name='account'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('profile/', profile, name='profile'),
    path("remove_land/<int:id>", remove_land, name="remove_land"),
]