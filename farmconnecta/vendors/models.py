from __future__ import unicode_literals
from django.utils import timezone
from django.db import models

# Create your models here.


class Vendors(models.Model):
    user = models.ForeignKey('auth.User')
    name = models.CharField(max_length=255)
    description = models.TextField()
    latitude = models.DecimalField(max_digits=20, default=0.00, decimal_places=6)
    longitude = models.DecimalField(max_digits=20, default=0.00, decimal_places=6)
    images = models.ImageField(upload_to='vendors', blank=True)
    created = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(
        blank=True, null=True
    )

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name

