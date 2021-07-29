from rest_framework import serializers
from hotel.models import HotelListings , HotelDescription

class HotelListingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelListings
        fields = '__all__'


class HotelDescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelDescription
        fields = '__all__'
