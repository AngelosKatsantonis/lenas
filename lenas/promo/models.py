from django.db import models
from django.urls import reverse

from easy_thumbnails.fields import ThumbnailerImageField
from ckeditor_uploader.fields import RichTextUploadingField

class Service(models.Model):
    title = models.CharField(max_length=1000, blank=False)
    description = RichTextUploadingField()
    image = ThumbnailerImageField(upload_to='promo-images/')

    class Meta:
        ordering = ['title']

    def __str__(self):
        return '%s'  % (self.title)

    def get_absolute_url(self):
        return reverse('promo:service', kwargs={'id': self.id})
