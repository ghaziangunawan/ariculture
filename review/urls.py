from django.urls import path
from review.views import show_review
from review.views import create_review
from review.views import show_json, profile_user, save_review

app_name = 'review'

urlpatterns = [
    path('', show_review, name='show_review'),
    path('create/', create_review, name='create_review'),
    path('json/', show_json, name='show_json'),
    path('profile_user/<str:user>/', profile_user, name='profile_user')
    path('save_review/', save_review, name='save_review')
]