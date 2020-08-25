from .models import Service

def get_services(request):
    return {'services': Service.objects.all() or None}
