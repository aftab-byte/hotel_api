from django.contrib import admin
from userapi.models import UserDetail ,HotelDetail , Profile
# Register your models here.
class ItemUserDetail(admin.ModelAdmin):
    list_display = ("name", "email","phone")

class ItemHotelDetail(admin.ModelAdmin):
    list_display = ("place", "price")

class ItemProfile(admin.ModelAdmin):
    list_display = ("phone", "otp")
    
admin.site.register(UserDetail ,ItemUserDetail)
admin.site.register(HotelDetail ,ItemHotelDetail)
admin.site.register(Profile ,ItemProfile)
