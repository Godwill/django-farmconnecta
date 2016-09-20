from __future__ import unicode_literals
from django.utils import timezone
from django.db import models


# Create your models here.
class VendorProduct(models.Model):
    user = models.ForeignKey('auth.User')
    vendor = models.ForeignKey('vendors.Vendors', null=True, blank=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=20, default=0.00, decimal_places=2)
    images = models.ImageField(upload_to='products', blank=True)
    created = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(
        blank=True, null=True
    )

    category_choices = (
        ('Vehicles', (
            ('Tractor', 'Tractor'),
            ('Truck', 'Truck'),
            )
        ),
        ('Feed', 'Feed'),
        ('Fertilizer', 'Fertilizer'),
        ('Seeds', 'Seeds'),
    )

    category = models.CharField(
        max_length=255,
        choices=category_choices,
        blank=False,
        default='None'
    )

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

