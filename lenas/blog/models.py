from django.db import models
from django.urls import reverse

from ckeditor_uploader.fields import RichTextUploadingField
from easy_thumbnails.fields import ThumbnailerImageField

class Article(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=1000, blank=False)
    description = models.CharField(max_length=10000, blank=True)
    content = RichTextUploadingField()
    image = ThumbnailerImageField(upload_to='article-images/')

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return '%s'  % (self.title)

    def get_absolute_url(self):
        return reverse('articles:article', kwargs={'id': self.id})
