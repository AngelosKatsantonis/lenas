from django.urls import path

from . import views

app_name = 'promo'

urlpatterns = [
    path('<id>/', views.get_service, name='service'),
]

