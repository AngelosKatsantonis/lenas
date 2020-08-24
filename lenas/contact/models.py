from django.db import models

from lenas.promo.models import Service

class Message(models.Model):
    fullname = models.CharField(max_length=250, blank=False)
    email = models.EmailField()
    phone = models.CharField(max_length=50, blank=False)
    subject = models.CharField(max_length=250, blank=False)
    message = models.CharField(max_length=250, blank=False)
    date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-date']

    def __str__(self):
        return '%s %s'  % (self.date, self.subject)

class Appointment(models.Model):
    #SERVICE_CHOICES = [x.title for x in Service.objects.all().items()]
    SERVICE_CHOICES = [('service1','service1'),('service2','service2')]

    fullname = models.CharField(max_length=250, blank=False)
    email = models.EmailField()
    phone = models.CharField(max_length=50, blank=False)
    description = models.CharField(max_length=250, blank=False, default="Please provide a simple description of your case and your goals.")
    date = models.DateTimeField(auto_now_add=True)
    appointment_date = models.DateTimeField()
    appointment_service = models.CharField(max_length=250, blank=False, choices=SERVICE_CHOICES)
    
    class Meta:
        ordering = ['-date']

    def __str__(self):
        return '%s %s'  % (self.appointment_date, self.appointment_service)
