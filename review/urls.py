from django.urls import path
from review.views import show_review
from review.views import create_review
from review.views import show_json
from review.views import *

app_name = 'review'

urlpatterns = [
    path('', show_review, name='show_review'),
    path('create/', create_review, name='create_review'),
    path('json/', show_json, name='show_json'),
    path('json/<str:user>/', review_user_json, name='review_user_json'),
]