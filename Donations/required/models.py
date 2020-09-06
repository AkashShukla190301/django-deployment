from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.

class Requirement(models.Model):
    REQUIRED_FOR = (
    ('NGO', 'NGO'),
    ('SELF', 'SELF')
    )

    name = models.CharField(max_length=128)
    
   
    Required_For = models.CharField(max_length=100, choices=REQUIRED_FOR, default='NGO')
    Ngo_name = models.CharField(max_length=123)
    Phone = models.PositiveIntegerField(blank=False)
    email = models.EmailField()