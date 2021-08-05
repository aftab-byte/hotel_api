from django.db import models

# Create your models here.
class Details(models.Model):
    Hotel_id = models.IntegerField(primary_key=True)
    Hotel_title = models.CharField(max_length=50)
    price = models.JSONField()
    image = models.ImageField()
    location = models.CharField(max_length=75)

    def __str__(self):
        return self.Hotel_title

class HotelDescription(models.Model):
    Hotel_id = models.ForeignKey(Details , on_delete=models.CASCADE)
    Amenties = models.JSONField()
    description = models.TextField()
    photo_1 = models.ImageField(blank=True)
    photo_2 = models.ImageField(blank=True)
    photo_3 = models.ImageField(blank=True)
    photo_4 = models.ImageField(blank=True)

    def __str__(self):
        return self.description[:10]
