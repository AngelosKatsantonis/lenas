from django.contrib import admin

from .models import Location 

# Register your models here

@admin.register(Location)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['area']

