

#  Create your models here
from django.db import models
from django.urls import reverse


# # Create your models here.




class BookDetail(models.Model):
    
    STANDARD_CHOICES = (
    ('primary_school', 'PRIMARY SCHOOL'),
    ('secondary_school', 'SECONDARY SCHOOL')
    )

    CONDITION_BOOKS = (
    ('good', 'GOOD'),
    ('average', 'AVERAGE'),
    ('bad', 'BAD')
    )


    name = models.CharField(max_length=246)
    author = models.CharField(max_length=246)
    standard = models.CharField(max_length=100, choices=STANDARD_CHOICES, default='PRIMARY SCHOOL')
    condition = models.CharField(max_length=100, choices=CONDITION_BOOKS, default='GOOD')

    book_photo = models.ImageField(upload_to="book_photos", blank=True)

    def get_absolute_url(self):
        return reverse("donate:address_detail")


class AddressDetail(models.Model):
    name = models.CharField(max_length=246, blank=False)
    email = models.EmailField(max_length=254, blank=False)
    Address = models.CharField(max_length=246, blank=False)
    city = models.CharField(max_length=246, default='Dehradun')
    Phone = models.PositiveIntegerField(blank=False)




