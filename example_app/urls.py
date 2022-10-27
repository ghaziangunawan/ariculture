from django.urls import path
from example_app.views import index
from example_app.views import register
from example_app.views import login_user
from example_app.views import logout_user

app_name = 'example_app'

urlpatterns = [
    path('', index, name='index'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
]