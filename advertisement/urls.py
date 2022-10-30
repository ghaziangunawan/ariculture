from django.urls import path, include
from advertisement.views import AdvertisementViewset, show_advertisement
from advertisement.views import show_json
from advertisement.views import AdvertisementSerializer
from rest_framework import routers

router = routers.DefaultRouter()
router.register('AdvertisementViewSet', AdvertisementViewset)


app_name = 'advertisements'

urlpatterns = [
    path('', show_advertisement, name='show_advertisement'),
    path('json/', show_json, name='show_json'),
    path('api/' , include(router.urls)),
]