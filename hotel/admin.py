from django.contrib import admin
from hotel.models import Booking ,HotelListings ,HotelDescription
# Register your models here.
admin.site.register(Booking)
admin.site.register(HotelListings)
admin.site.register(HotelDescription)
