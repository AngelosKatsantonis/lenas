from django.urls import path

from . import views

app_name = 'home'

urlpatterns = [
    path('', views.get_home, name='home'),
    # Need to hook to appropriate view
    path('info', views.get_home, name='info'),
]
