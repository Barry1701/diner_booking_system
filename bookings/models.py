from django.db import models
from django.contrib.auth.models import User


# Informations about bookings in restaurant 'Piast'
class Booking(models.Model):
    date = models.DateField()
    time = models.TimeField()
    number_of_guests = models.PositiveIntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Booking #{self.pk} - {self.date} at {self.time} for {self.number_of_guests} guests"



#This model represents whats on menu this week in 'Piast'
class Menu(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name


