# Generated by Django 3.1 on 2020-08-19 12:52

import ckeditor_uploader.fields
from django.db import migrations, models
import easy_thumbnails.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=1000)),
                ('description', models.CharField(blank=True, max_length=10000)),
                ('content', ckeditor_uploader.fields.RichTextUploadingField()),
                ('image', easy_thumbnails.fields.ThumbnailerImageField(upload_to='article-images/')),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
    ]
