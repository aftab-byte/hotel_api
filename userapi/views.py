from django.shortcuts import render ,redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from .models import UserDetail ,Profile ,HotelDetail
import os
from twilio.rest import Client
import random
import jwt

from userapi.serializers import UserDetailSerializer ,HotelDetailSerializer
# Create your views here.
otp = random.randint(100000,999999)
class Register(APIView):
    def send_otp(self , phone ,otp):
        print("send_otp is called")
        # Find your Account SID and Auth Token at twilio.com/console
        # and set the environment variables. See http://twil.io/secure
        account_sid = 'ACcd0432425fbd8f4d1e87fb25e9fce7b6'
        auth_token = '05cc64529a27dd4392d887a81d8e80af'
        client = Client(account_sid, auth_token)

        message = client.messages \
                        .create(
                             body=f'Your login otp is {otp}',
                             from_='+14352161497',
                             to='+918400842036'
                         )
        print(message.sid)
        return None

    def post(self,request):
        name = request.data['name']
        email = request.data['email']
        phone = request.data['phone']

        check_phone = UserDetail.objects.filter(phone = phone).first()
        check_email = UserDetail.objects.filter(email=email)
        if check_phone:
            return Response({'message':'This mobile number already exist'})
        if check_email:
            return Response({'message':'This email already exist'})
        serializer = UserDetailSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status':'true','message':'you are registered succesfully'})

        # self.send_otp(phone,otp)
        # profile = Profile(phone = phone ,otp = otp)
        # profile.save()
        # request.session['phone'] = phone
        #redirect('OtpVerification')
        else:
            return Response({'status':'False','message':'your credentials are not valid'})



class OtpVerification(APIView):
    def post(self,request):
        phone = request.session['phone']
        otp_check = request.data['otp']
        user = UserDetail.objects.filter(phone = phone)
        profile = Profile.objects.filter(phone = phone).last()

        if otp_check != profile.otp:
            return Response({'status':'False','message':'otp is wrong'})


        else:
            #return Response({'status':'True','message':'otp verified'})

            payload = {
                'id':profile.id,
                'phone':profile.phone
            }

            token = jwt.encode(payload ,key = "donottellanyone",algorithm='HS256').decode('utf-8')
            response = Response()
            response.set_cookie(key='jwt',value = token, httponly = True)
            response.data = {
            'status':'True',
            'jwt':token,
            'message':'otp verified'
            }
            return response


        # return Response({'message':'Saved succesfully in database'})

class Login(APIView):
    def send_otp(self , phone ,otp):
        print("send_otp is called")
        # Find your Account SID and Auth Token at twilio.com/console
        # and set the environment variables. See http://twil.io/secure
        account_sid = 'ACcd0432425fbd8f4d1e87fb25e9fce7b6'
        auth_token = '05cc64529a27dd4392d887a81d8e80af'
        client = Client(account_sid, auth_token)

        message = client.messages \
                        .create(
                             body=f'Your login otp is {otp}',
                             from_='+14352161497',
                             to='+918400842036'
                         )
        print(message.sid)
        return None

    def post(self,request):
        phone = request.data['phone']
        phone_check  = UserDetail.objects.filter(phone = phone).first()
        if phone_check is None:
            return ({'message':'This number is not registered'})

        self.send_otp(phone,otp)
        profile = Profile(phone = phone ,otp = otp)
        profile.save()
        request.session['phone'] = phone
        return Response({'status':'true','message':'otp is send to you'})

class HotelDetailView(APIView):
    def get(self,request):
        token = request.COOKIES.get('jwt')
        print(token)
        if not token:
            raise AuthenticationFailed('Unauthenticated')
        try:
            payload = jwt.decode(jwt = token ,key="donottellanyone")
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated')

        hotel = HotelDetail.objects.all()
        serializer =HotelDetailSerializer(hotel ,many=True)
        return Response(serializer.data)
class Logout(APIView):
    def post(self,request):
        response = Response()
        response.delete_cookie('jwt')
        response.data ={
            'message': 'Succesfully Logout'
        }

        return response
