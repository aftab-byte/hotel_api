from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from hotelapi.models import Details ,HotelDescription
from hotelapi.serializers import DetailsSerializer , HoteldescSerializer
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

class DescriptionAPI(APIView):
    '''lets use exceptions handling using try and except to handle error(TypeError/Doesnot exist) if no data is found for corresponding key'''
    def get_object(self, pk):
        try:
            return HotelDescription.objects.get(pk=pk)
        except HotelDescription.DoesNotExist:
            return None
    def get(self ,request ,pk , format = None):
        print(id)
        desc = self.get_object(pk)
        if desc:
            print(desc)
            serializer = HoteldescSerializer(desc ,many = False)
            return Response(serializer.data)
        else:
            return Response({'response':'details for corrresponding id does not exist'},status = status.HTTP_400_BAD_REQUEST)
