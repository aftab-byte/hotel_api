from rest_framework import serializers
from hotelapi.models import Details ,HotelDescription

class DetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Details
        fields = '__all__'

class HoteldescSerializer(serializers.ModelSerializer):
    Hotel_id = DetailsSerializer()
    class Meta:
        model = HotelDescription
        fields = '__all__'
        depth = 1
