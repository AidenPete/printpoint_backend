from django.db import models
from accounts.models import User

class DeliveryAddress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)
    country = models.CharField(max_length=100)
    is_default = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.street}, {self.city}, {self.country}"

class PickupLocation(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name