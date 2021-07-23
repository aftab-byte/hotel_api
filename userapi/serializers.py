from rest_framework import serializers
from userapi.models import UserDetail ,Profile ,HotelDetail


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDetail
        fields = '__all__'

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'

class HotelDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelDetail
        fields = '__all__'
