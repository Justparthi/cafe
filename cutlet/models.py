from django.db import models

class Place(models.Model):
    name = models.CharField(max_length=2555)
    map_url = models.URLField(max_length=5005)
    img_url = models.URLField(max_length=5005)
    location = models.CharField(max_length=2555)
    has_sockets = models.CharField(max_length=6969)
    has_toilet = models.CharField(max_length=6969)
    has_wifi = models.CharField(max_length=6969)
    can_take_calls = models.CharField(max_length=6969)
    seats = models.CharField(max_length=255)
    coffee_price = models.CharField(max_length=255)
    stable_wifi = models.CharField(max_length=100)
    power_sockets = models.CharField(max_length=100)
    quiet = models.CharField(max_length=100)
    calls = models.CharField(max_length=100)
    tables = models.CharField(max_length=100)
    coffee = models.CharField(max_length=100)
    food = models.CharField(max_length=100)
    veggie = models.CharField(max_length=100)
    payment = models.CharField(max_length=100)
    
    restroom = models.CharField(max_length=100)
    def __str__(self):
        return self.name
