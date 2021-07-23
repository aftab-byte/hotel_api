from django.db import models

# Create your models here.
class UserDetail(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    phone = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class Profile(models.Model):
    phone = models.CharField(max_length=10)
    otp = models.IntegerField()

class HotelDetail(models.Model):
    place = models.CharField(max_length=100)
    price = models.IntegerField()

    def __str__(self):
        return self.place
