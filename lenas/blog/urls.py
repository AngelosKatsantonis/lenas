from django.urls import path

from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.get_articles, name='articles'),
    path('<id>/', views.get_article, name='article'),
]

