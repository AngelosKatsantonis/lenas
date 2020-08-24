from django.shortcuts import render

from .contactforms import AppointmentForm

# Create your views here.
def get_appointment(request):
    form  = AppointmentForm(request.POST or None, label_suffix='')
    success = False
    if form.is_valid():
        form.save()
        success = True
        form = AppointmentForm()
    context = {
        'form': form,
        'success': success,
    }
    return render(request, 'contact/appointmentform.html', context)
