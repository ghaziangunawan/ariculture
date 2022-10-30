from django.urls import path
from homepage.views import index
from homepage.views import register
from homepage.views import login_user
from homepage.views import logout_user
from homepage.views import show_advertisement_user, create_ad, set_remove

app_name = 'homepage'

urlpatterns = [
    path('', index, name='index'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('Advertising/', show_advertisement_user, name='advertise'),
    path('Create_Advert/', create_ad, name='create_advert'),
    path("set_remove/<int:id>", set_remove, name="set_remove"),
]