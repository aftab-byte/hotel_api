from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from hotelapi.models import Details
from hotelapi.serializers import DetailsSerializer
# Create your views here.

# Create your views here.
'''get request to retreive list of hotels'''
class DetailsView(APIView):
    def get(self ,request ,format = None ):
        '''if I get location coordinates then i have to convert into exact city locatio
        using geolocation package or calculate just nearcy and sort it'''
        #listing = HotelListings.objects.filter(location__icontains = "kashmir")
        listing = Details.objects.all()
        print(listing)
        if listing:
            serializer = DetailsSerializer(listing ,many=True)
            return Response(serializer.data , status = status.HTTP_200_OK)
        else:
            return Response({'status':'False','message':'No Hotel for this location'} ,status = status.HTTP_400_BAD_REQUEST)
