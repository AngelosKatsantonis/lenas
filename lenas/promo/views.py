from django.shortcuts import render,get_object_or_404

from .models import Service
from lenas.contact.contactforms import AppointmentForm

# Create your views here.

def get_service(request, id):
    service = get_object_or_404(Service, id=id)
    form  = AppointmentForm(request.POST or None, label_suffix='')
    form.appointment_service = service.title
    success = False
    if form.is_valid():
        form.save()
        success = True
        form = AppointmentForm()
    context = {
        'form': form,
        'success': success,
        'service': service
    }
    return render(request, 'promo/service.html', context)
