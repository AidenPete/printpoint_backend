from django.db import models
from accounts.models import User
from orders.models import DeliveryAddress, PickupLocation

class Document(models.Model):
    PAPER_SIZES = [
        ('A4', 'A4'),
        ('A3', 'A3'),
        ('Letter', 'Letter'),
        ('Legal', 'Legal'),
    ]
    
    PRINT_TYPES = [
        ('color', 'Color'),
        ('bw', 'Black & White'),
    ]
    
    SIDES = [
        ('single', 'Single-sided'),
        ('double', 'Double-sided'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.FileField(upload_to='documents/')
    original_filename = models.CharField(max_length=255)
    file_type = models.CharField(max_length=50)
    color = models.CharField(max_length=10, choices=PRINT_TYPES, default='bw')
    paper_size = models.CharField(max_length=10, choices=PAPER_SIZES, default='A4')
    pages_per_sheet = models.PositiveIntegerField(default=1)
    copies = models.PositiveIntegerField(default=1)
    sides = models.CharField(max_length=10, choices=SIDES, default='single')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.original_filename

class PrintJob(models.Model):
    STATUS_CHOICES = [
        ('uploaded', 'Uploaded'),
        ('in_progress', 'In Progress'),
        ('ready', 'Ready'),
        ('delivered', 'Delivered'),
    ]
    
    DELIVERY_METHODS = [
        ('delivery', 'Delivery'),
        ('pickup', 'Pickup'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    documents = models.ManyToManyField(Document)
    delivery_method = models.CharField(max_length=10, choices=DELIVERY_METHODS)
    delivery_address = models.ForeignKey(DeliveryAddress, on_delete=models.SET_NULL, null=True, blank=True)
    pickup_location = models.ForeignKey(PickupLocation, on_delete=models.SET_NULL, null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='uploaded')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    payment_reference = models.CharField(max_length=255, blank=True, null=True)
    payment_method = models.CharField(max_length=50, blank=True, null=True)
    payment_completed = models.BooleanField(default=False)
    
    def __str__(self):
        return f"PrintJob #{self.id} - {self.user.email}"