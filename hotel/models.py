from django.db import models
from datetime import datetime
# Create your models here.
class HotelListings(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=7 ,decimal_places=2)
    location = models.JSONField()
    pin_code = models.CharField(max_length=7)
    image =models.ImageField(upload_to='image')

    def __str__(self):
        return self.title

class HotelDescription(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=50)
    location = models.JSONField()
    amenties = models.JSONField()
    price = models.DecimalField(max_digits=7,decimal_places=2)
    description = models.TextField(max_length=300)
    photo_main = models.ImageField(upload_to='description')
    photo_1 = models.ImageField(upload_to='description')
    photo_2 = models.ImageField(upload_to='description')
    photo_3 = models.ImageField(upload_to='description')
    photo_4 = models.ImageField(upload_to='description')
    photo_5 = models.ImageField(upload_to='description')

    def __str__(self):
        return self.title

class Booking(models.Model):
    adhar_no = models.CharField(max_length=12)
    STAY_CHOICES = [
    ('Long', 'Long_Stay'),
    ('Short', 'Short_Stay')
    ]
    stay_type = models.CharField( max_length=10,
        choices=STAY_CHOICES,
        default='Short')
    name = models.CharField(max_length=25)
    phone_number = models.CharField(max_length=10)
    email = models.EmailField()
    booking_date = models.DateTimeField(default = datetime.now)

    def __str__(self):
        return self.adhar_no
