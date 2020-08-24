from django.contrib import admin

from .models import Message,Appointment 

# Register your models here

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ['date','email','subject']

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ['date','email','appointment_date','appointment_service']
