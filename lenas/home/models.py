from django.db import models

class Location(models.Model):
    address = models.CharField(max_length=100, blank=False)
    area = models.CharField(max_length=40, blank=False)
    latitude = models.CharField(max_length=40, blank=False)
    longitude = models.CharField(max_length=40,blank=False)
    phone = models.CharField(max_length=40,blank=True)

    class Meta:
        ordering = ['area']

    def __str__(self):
        return '%s'  % (self.address)
