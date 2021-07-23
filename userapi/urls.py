from django.contrib import admin
from django.urls import path,include
from userapi import views
urlpatterns = [

    path('register',views.Register.as_view()),
    path('verify',views.OtpVerification.as_view(),name='OtpVerification'),
    path('login',views.Login.as_view(),name='login'),
    path('detail',views.HotelDetailView.as_view(),name='detail'),
    path('logout',views.Logout.as_view(),name='logout'),


]
