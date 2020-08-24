from django.shortcuts import render

from lenas.settings import GOOGLE_API_KEY as GAK

from lenas.blog.models import Article
from lenas.promo.models import Service
from lenas.contact.contactforms import ContactForm
from .models import Location

# Create your views here.

def get_home(request):
    articles = Article.objects.all()[:4]
    offices = Location.objects.all()
    form = ContactForm(request.POST or None, label_suffix='')
    success = False
    if form.is_valid():
        form.save()
        success = True
        form = ContactForm()
    context = {
        'articles': articles,
        'form': form,
        'success': success,
        'offices': offices,
        'GAK': GAK
    }
    return render(request, 'home/home.html', context)

def get_info(request):
    return render(request, 'home/home.html', context)
    pass
