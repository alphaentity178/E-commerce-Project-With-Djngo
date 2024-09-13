from django.db import models
from django.conf import settings

# Create your models here.

class BillingAddress(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    address = models.CharField(max_length=264, blank=True)
    zipcode = models.CharField(max_length=10, blank=True)
    city = models.CharField(max_length=100, blank=True)
    country = models.CharField(max_length=50, blank=True)
    
    def __str__(self):
        return f"{self.user.username}'s billing address"
    
    def is_fully_filled(self):
        required_fields = ['address', 'zipcode', 'city', 'country']
        for field in required_fields:
            value = getattr(self, field)
            if not value:
                return False
        return True
    
    class Meta:
        verbose_name_plural = "Billing Addresses"