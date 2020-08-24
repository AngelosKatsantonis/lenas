from django import forms

from .models import Message,Appointment

class ContactForm(forms.ModelForm):
        class Meta:
            model = Message
            fields = [
                'fullname',
                'email',
                'phone',
                'subject',
                'message',                                                                      ]
            labels = {'fullname': 'Full name'}

class AppointmentForm(forms.ModelForm):
        class Meta:
            model = Appointment
            fields = [
                'fullname',
                'email',
                'phone',
                'appointment_date',
                'description',
            ]
            
            labels = {'fullname': 'Full name'}
            widgets = {
                'description': forms.Textarea(),
                'appointment_date': forms.DateTimeInput() 
            }
