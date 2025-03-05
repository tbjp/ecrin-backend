from django.db import models
from properties.models import Property

class Booking(models.Model):
    BOOKING_STATUS = (
        ('active', 'Active'),
        ('future', 'Future'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    )

    property = models.ForeignKey(Property, related_name='bookings', on_delete=models.CASCADE)
    guest_name = models.CharField(max_length=100)
    check_in = models.DateField()
    check_out = models.DateField()
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=10, choices=BOOKING_STATUS, default='future')

    def __str__(self):
        return f"{self.guest_name} - {self.property.name}"
