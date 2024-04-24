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

class Table(models.Model):
    number = models.PositiveIntegerField(unique=True)
    capacity = models.PositiveIntegerField()

    def __str__(self):
        return f"Stolik #{self.number} (Pojemność: {self.capacity})"

class Reservation(models.Model):
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Rezerwacja dla {self.user} przy stoliku #{self.table.number} na {self.booking.date} o godzinie {self.booking.time}"



