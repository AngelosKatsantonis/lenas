# Generated by Django 3.1 on 2020-08-19 20:20

from django.db import migrations, models
import easy_thumbnails.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1000)),
                ('description', models.CharField(blank=True, max_length=10000)),
                ('image', easy_thumbnails.fields.ThumbnailerImageField(upload_to='promo-images/')),
            ],
            options={
                'ordering': ['title'],
            },
        ),
    ]
