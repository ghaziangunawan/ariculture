from homepage.models import Advertisement
from rest_framework import serializers

class AdvertisementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advertisement
        fields = '__all__'
        depth = 1